from flask import request, jsonify, redirect
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_raw_jwt, get_jwt_identity
from models import MedicalRecordsModel, PatientModel
import datetime
import json


def parse_date(string_date):
    string_list = string_date.split("-")
    date = datetime.date(int(string_list[0]), int(string_list[1]), int(string_list[2]))
    return date


class Patient(Resource):
    @jwt_required
    def get(self):
        # data = [patient.json() for patient in PatientModel.find_all()]
        return 200

    @jwt_required
    def post(self):
        string_req = request.get_data()
        data = json.loads(string_req)
        new_patient = PatientModel(
            data['firstname'], 
            data['lastname'], 
            parse_date(data['date_birth']),
            data['birth_place'],
            data['tax_code'],
            is_hospitalized=False)
        new_patient.add_to_db()
        return {'message': 'Patient Successfully Inserted'}, 200

    @jwt_required
    def delete(self, id):
        claims = get_raw_jwt()['jti']
        if not claims['is_admin']:
            return jsonify({"message", "Admin required"})
        patient = PatientModel.find_id(id=id)
        if patient:
            patient.delete_from_db()
            return jsonify({'message': 'Patient Deleted Successfully'}), 200
        return jsonify({'messase': f'Patient {patient.firstname} not found'}), 404


class PatientList(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        all_patients = [patient.json() for patient in PatientModel.find_all()]
        
        if user_id:
            return json.dumps({'patients': all_patients})
    
        return json.dumps({'message': 'Invalid credentials'}), 401


class MedicalRecords(Resource):
    @classmethod
    def post(cls):
        data_str = request.get_data()
        data = json.loads(data_str)

        new_medical_records = MedicalRecordsModel()


