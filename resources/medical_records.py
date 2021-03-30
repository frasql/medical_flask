from flask import request, jsonify, redirect
from flask_restful import Resource
from models import MedicalRecordsModel, PatientModel
import datetime
import json


class MedicalRecord(Resource):
    @classmethod
    def get(cls, patient_id: int):
        data_string = request.get_data()
        data = json.loads(data_string)


    @classmethod
    def post(cls, patient_id: int):
        data_string = request.get_data()
        data = json.loads(data_string)

        patient = PatientModel.find_by_id(patient_id)
        
        if patient.medical_records:
            return json.dumps({"message": "Medical Records already exists"})
        
        new_medical_records = MedicalRecordsModel(
            data["date_admission"],
            data["first_diagnosis"],
            data["last_diagnosis"],
            data["date_discharge"]
        )

        patient.medical_records = new_medical_records

        patient.add_to_db()
        return json.dumps({"message": "Medical Records Successfully Created"})