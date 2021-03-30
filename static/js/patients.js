function FetchPatients() {
// Fetch Patients
    let options = {
        method: 'GET',
        mode: 'cors',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access_token')}`
        }  
    }

    const url = 'http://localhost:5000/patients/';

    req = new Request(url, options);

    fetch(req)
    .then((resp) => {
        if(resp.ok) {
            return resp.json();
        } else {
            throw new Error();
        }
    })
    .then((data) => {
        let json_data = JSON.parse(data);
        let patients = json_data['patients'];
        let output = '';
        console.log(patients);
        patients.forEach(patient => {
            let tbody = document.querySelector("#patient_row");
            output = 
            `
                <td>${patient['firstname']}</td>
                <td> ${patient['lastname']}</td>
                <td>${patient['date_birth']}</td>
                <td> ${patient['birth_place']}</td>
                <td>${patient['tax_code']}</td>
                <td><a class="button" href="/medical_records/${patient["id"]}" id="medical_records">medical_records</a></td>                
            `
            row = document.createElement('tr');

            row.innerHTML = output;

            tbody.appendChild(row);
        
        });

    })
    .catch((error) => {
        console.log("Error:", error);
    })

}


function InsertPatient() {
        // field values
        const firstname = document.querySelector("#firstname").value;
        const lastname = document.querySelector("#lastname").value;
        const date_birth = document.querySelector("#date_birth").value;
        const birth_place = document.querySelector("#birth_place").value;
        const tax_code = document.querySelector("#tax_code").value;

        let data = {
            'firstname': firstname,
            'lastname': lastname, 
            'date_birth': date_birth,
            'birth_place': birth_place,
            'tax_code': tax_code
        };

        let options = {
            method: 'POST',
            mode: 'cors',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            },
            body: JSON.stringify(data)
        }
        
        const url = 'http://localhost:5000/patient/';
        
        req = new Request(url, options);
        
        fetch(req)
        .then((resp) => {
            if(resp.ok) {
                return resp.json();
            } else {
                throw new Error();
            }
        })
        .then((data) => {
            console.log(data);

        })
        .catch((error) => {
            console.log("Error:", error);
        })
}

window.addEventListener('load', FetchPatients());


// Modal insert patient
const btn_insert_modal = document.querySelector('#open_insert_modal');
const modal_insert_patient = document.querySelector('#modal_insert_patient');
const close_insert_buttons = document.querySelector('.close_insert_buttons');


btn_insert_modal.addEventListener('click', () => {
    modal_insert_patient.classList.add('is-active');
});

close_insert_buttons.addEventListener('click', () => {
    modal_insert_patient.classList.remove('is-active');
});

// Fetch Patients
const btn_insert_patient = document.querySelector("#insert_patient");
if(btn_insert_patient) {
    btn_insert_patient.addEventListener('click', InsertPatient);
}