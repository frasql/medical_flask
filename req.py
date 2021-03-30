import requests
import datetime

date = datetime.date(2001, 2, 4)

data = {
    'firstname': 'francesco',
    'lastname': 'squillace',
    'date_birth': date
}

req = requests.post("http://localhost:5000/patient/", data=data)
print(req.status_code)