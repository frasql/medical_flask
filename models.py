from typing import List
import datetime
from db import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column('id', db.Integer(), primary_key=True)
    name = db.Column('name', db.Enum('admin', 'doctor', 'nurse', 'guest'), default='guest')
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer(), primary_key=True)
    username = db.Column('username', db.String(50), nullable=False, unique=True)
    firstname = db.Column('firstname', db.String(50), nullable=False)
    lastname = db.Column('lastname', db.String(50), nullable=False)
    password = db.Column('password', db.String(50), nullable=False)

    role = db.relationship("Role", backref="role", uselist=False)
    
    department_id = db.Column("department_id", db.ForeignKey('departments.id'))


    def __init__(self, username, firstname, lastname, password):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password


    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'password': self.password,
            'role': self.role,
            'department_id': self.department_id
        }

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.remove(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


class DepartmentModel(db.Model):
    __tablename__ = 'departments'
    id = db.Column('id', db.Integer(), primary_key=True)
    name = db.Column('name', db.String(80), unique=True, nullable=False)
    description = db.Column('description', db.String(255))
    users = db.relationship("User", backref="users", lazy='dynamic', passive_deletes=True)


    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'users': [user.json() for user in self.users],
        }

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.remove(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name) -> "DepartmentModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["DepartmentModel"]:
        return cls.query.all()



class PatientModel(db.Model):
    __tablename__ = 'patients'
    id = db.Column('id', db.Integer(), primary_key=True)
    firstname = db.Column('firstname', db.String(50), nullable=False)
    lastname = db.Column('lastname', db.String(50), nullable=False)
    date_birth = db.Column('date_birth', db.Date(), nullable=False)
    birth_place = db.Column('birth_place', db.String(255), nullable=False)
    tax_code = db.Column('tax_code', db.String(20), unique=True, nullable=False)
    is_hospitalized = db.Column('is_hospitalized', db.Boolean(), default=False)

    medical_records = db.relationship("MedicalRecordsModel", backref='medical_records', uselist=False)


    def __init__(self, firstname, lastname, date_birth, birth_place, tax_code, is_hospitalized):
        self.firstname = firstname
        self.lastname = lastname
        self.date_birth = date_birth
        self.birth_place = birth_place
        self.tax_code = tax_code
        self.is_hospitalized = is_hospitalized

    def json(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "date_birth": str(self.date_birth),
            "birth_place": self.birth_place,
            "tax_code": self.tax_code,
            "is_hospitalized": self.is_hospitalized
        }

    def fullname(self) -> str:
        fullname = f'{self.firstname} {self.lastname}'
        return fullname

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.remove(self)
        db.session.commit()

    @classmethod
    def search_patient(cls, firstname, lastname, date_birth) -> "PatientModel":
        patient = cls.query.filter(firstname).filter(lastname).filter(date_birth).first()
        return patient

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()


class MedicalRecordsModel(db.Model):
    __tablename__ = "medical_records"
    id = db.Column("id", db.Integer(), primary_key=True)
    date_of_admission = db.Column(db.DateTime(), default=datetime.datetime.utcnow, nullable=False)
    first_diagnosis = db.Column(db.Text(), nullable=False)
    last_diagnosis = db.Column(db.Text(), nullable=False)
    date_of_discharge = db.Column(db.DateTime(), nullable=False)

    patient_id = db.Column(db.Integer(), db.ForeignKey('patients.id'))


    def __init__(self, id, date_of_admission, first_diagnosis, last_diagnosis, date_of_discharge, patient_id):
        self.id = id
        self.date_of_admission = date_of_admission
        self.first_diagnosis = first_diagnosis
        self.last_diagnosis = last_diagnosis
        self.date_of_discharge = date_of_discharge
        self.patient_id = patient_id


    def json(self):
        return {
            "id": self.id,
            "date_of_admission": str(self.date_of_admission),
            "first_diagnosis": self.first_diagnosis,
            "last_diagnosis": self.last_diagnosis,
            "date_of_discharge": str(self.last_diagnosis),
            "patient_id":self.patient_id
        }

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.remove(self)
        db.session.commit()

    
    @classmethod
    def find_by_patient_id(cls, patient_id: int) -> "MedicalRecordsModel":
        return cls.query.filter_by(patient_id=patient_id).first()


