function FetchDepartments() {
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
    
        const url = 'http://localhost:5000/departments/';
    
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
            let departments = json_data['departments'];
            console.log(departments);
            let output = '';
            departments.forEach(department => {
                console.log(department);
                let columns = document.querySelector("#department_cards");
                output = 
                `
                    <div class="card-image">
                        <img src="#" alt="Placeholder image">
                    </div>
                    <div class="card-content">
                        <div class="content">
                            <p class="title">${department.name}</p>
                            <p class="subtitle">${department.description}</p>
                            <br>
                            <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
                        </div>
                    </div>
                `;
                row = document.createElement('div');
                row.classList.add("card");
                row.innerHTML = output;
                columns.appendChild(row);
            
            });
    
        })
        .catch((error) => {
            console.log("Error:", error);
        })
    
    }

window.addEventListener('load', FetchDepartments());
