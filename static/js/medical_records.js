function FetchMedicalRecords() {
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
    
        const url = 'http://localhost:5000/medical_records/';
    
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
            let patients = json_data['medical_records'];
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
    
    
function InsertMedicalRecords() {
            // field values
            const date_admission = document.querySelector("#date_admission").value;
            const first_diagnosis = document.querySelector("#first_diagnosis").value;
            const last_diagnosis = document.querySelector("#last_diagnosis").value;
            const date_discharge = document.querySelector("#date_discharge").value;
    
            let data = {
                'date_admission': date_admission,
                'first_diagnosis': first_diagnosis, 
                'last_diagnosis': last_diagnosis,
                'date_discharge': date_discharge
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
            
            const url = 'http://localhost:5000/medical_record/';
            
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
    
// window.addEventListener('load', FetchPatients());
    
    
// Modal insert medical record
const btn_medical_record_modal = document.querySelector('#open_medical_record_modal');
const modal_medical_record = document.querySelector('#modal_insert_medical_record');
const close_medical_record_buttons = document.querySelector('.close_medical_record_buttons');
    
    
btn_medica_record_modal.addEventListener('click', () => {
    modal_medical_record.classList.add('is-active');
});
    
close_medical_record_buttons.addEventListener('click', () => {
    modal_medical_record.classList.remove('is-active');
});