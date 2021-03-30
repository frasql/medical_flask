import unittest
from models import PatientModel
from config import BaseConfig
import datetime
from app import app


class Test(unittest.TestCase):

    def setUp(self):
        app.config.from_object(BaseConfig)

    def test_patient(self):
        date = datetime.date(2020, 2, 3)
        patient = PatientModel('francesco', 'lastname', date)
        self.assertEqual(patient.firstname, 'francesco')
        self.assertEqual(patient.lastname, 'lastname')


if __name__ == '__main__':
    unittest.main()
