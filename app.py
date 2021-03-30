from blacklist import BLACKLIST
from flask import Flask, render_template, url_for, redirect, request, g, jsonify
from db import db
from config import BaseConfig
from flask_restful import Api
from flask_migrate import Migrate
from resources.patients import Patient, PatientList
from resources.users import (
    TokenRefresh, 
    UserLogin, 
    UserLogout, 
    UserRegister
)
from resources.medical_records import MedicalRecord
from resources.departments import Department, DepartmentsList
from flask_jwt_extended import JWTManager, decode_token


app = Flask(__name__)
app.config.from_object(BaseConfig)

api = Api(app)

db.init_app(app)

migrate = Migrate(app, db)

jwt = JWTManager(app)


@app.before_request
def _get_token():
    auth_header = request.headers.get("Authorization")
    g.token = None
    if auth_header and "Bearer" in auth_header:
        jwt_token = auth_header.split(" ")[-1]
        g.token = decode_token(jwt_token)

"""
@jwt.token_in_blacklist_loader
def check_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'description': 'The token has expired',
        'error': 'token_expired'
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback():
    return jsonify({
        'description': "Signature verification failed",
        'error': 'invalid_token'
    }), 401

@jwt.unauthorized_loader
def unauthorized_callback():
    return jsonify({
        'description': "Token jwt required",
        'error': "missing_token"
    }), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({
        'description': "Token is not fresh",
        'error': "fresh_token_required"
    }), 401


@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        'description': "Token has been revoked",
        'error': "token_revoked"
    }), 401

"""

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/show_departments/')
def show_departments():
    return render_template('show_departments.html')

@app.route("/doctors/")
def doctors():
    return render_template('doctors/doctors.html')

@app.route('/show_patients/')
def show_patients():
    return render_template('show_patients.html')

@app.route('/show_medical_records/')
def show_medical_records():
    return render_template('show_medical_records.html')


api.add_resource(UserRegister, '/register/')
api.add_resource(UserLogin, '/login/')
api.add_resource(UserLogout, '/logout/')
api.add_resource(TokenRefresh, '/token_refresh/')

api.add_resource(Patient, '/patient/')
api.add_resource(PatientList, '/patients/')
api.add_resource(MedicalRecord, '/medical_record/')

api.add_resource(DepartmentsList, '/departments/')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
