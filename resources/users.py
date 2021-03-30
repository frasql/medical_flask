import flask_jwt_extended
from blacklist import BLACKLIST
from flask import request, jsonify
from flask_jwt_extended.utils import get_jti, get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_required
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource
from models import User
from werkzeug.security import safe_str_cmp
import json


class UserRegister(Resource):
    def post(self):
        data_string = request.get_data()
        data = json.loads(data_string)
        print(data)
        firstname = data['firstname']
        lastname = data['lastname']
        username = data['username']
        password = data['password']

        # create a role for each user
        # create a department for each user

        user = User(username=username, firstname=firstname, lastname=lastname, password=password)

        user.add_to_db()
        return jsonify({'message': f'User {username} successfully registered'})


class UserLogin(Resource):
    @classmethod
    def post(cls):
        # get data 
        data_string = request.get_data()
        # parse data
        data = json.loads(data_string)
        username = data['username']
        password = data['password']

        print(data)
        # find user
        user = User.find_by_username(username=username)
        print(user)
        if not user:
            return jsonify({'message': f"User {user.username} not found"}), 404
        
        # check password
        if user.password == password:
            # create jwt
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return json.dumps({
                'access_token': access_token,
                'refresh_token': refresh_token
            }), 200

        return json.loads({'message': 'invalid credentials'})


class UserLogout(Resource):
    @jwt_required
    def post(self):
        jti = get_jti()
        BLACKLIST.add(jti)
        return jsonify({
            'message': 'Successfully logged out'
        })



class TokenRefresh(Resource):
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        # create fresh token
        new_token = create_access_token(identity=current_user, fresh=False)
        return jsonify({'access_token': new_token}), 200
