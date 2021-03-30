from flask import request, jsonify, redirect
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_raw_jwt, get_jwt_identity
from models import DepartmentModel
import datetime
import json


def parse_date(string_date):
    string_list = string_date.split("-")
    date = datetime.date(int(string_list[0]), int(string_list[1]), int(string_list[2]))
    return date


class Department(Resource):
    @jwt_required
    def get(self):
        # data = [patient.json() for patient in PatientModel.find_all()]
        return 200

    @jwt_required
    def post(self):
        string_req = request.get_data()
        data = json.loads(string_req)
        new_patient = DepartmentModel(data['name'], data['description'])
        new_patient.add_to_db()
        return {'message': 'Department Successfully Inserted'}, 200

    @jwt_required
    def delete(self, id):
        claims = get_raw_jwt()['jti']
        if not claims['is_admin']:
            return jsonify({"message", "Admin required"})
        patient = DepartmentModel.find_by_name(name=claims['name'])
        if patient:
            patient.delete_from_db()
            return jsonify({'message': 'Patient Deleted Successfully'}), 200
        return jsonify({'messase': f'Patient {patient.firstname} not found'}), 404


class DepartmentsList(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        all_departments = [department.json() for department in DepartmentModel.find_all()]
        
        if user_id:
            return json.dumps({'departments': all_departments})
    
        return json.dumps({'message': 'Invalid credentials'}), 401
