btn_add_patient = document.querySelector('#btn-add-patient');

firstname = document.getElementById('firstname');
lastname = document.getElementById('lastname');
date_birth = document.getElementById('date_birth');

btn_add_patient.addEventListener('click', () => {
    console.log(btn_add_patient);
    console.log(firstname.value, lastname.value, date_birth.value);

    data = {
        'firstname': firstname.value,
        'lastname': lastname.value,
        'date_birth': date_birth.value
    }

    console.log(data);
    let h = new Headers();
    h.append('content-type', 'application-json');


    let options = {
        method: 'POST',
        mode: 'cors',
        header: h,
        body: JSON.stringify(data)
        
    }

    url = 'http://localhost:5000/patient/';

    req = new Request(url, options);

    fetch(req)
    .then((response) => {
        if(response.ok) {
            return response.json();
        } else {
            throw new Error();
        }
    })
    .then((data) => {
        console.log(data);
    })
    .catch((err) => {
        console.log("Error:", err);
    })



});


// modal signup

const signUpButton = document.querySelector('#signup');

if(signUpButton) {
    
    const modal_signup = document.querySelector('#modal-signup');
    const closeSignupBtn = document.querySelector('#close-signup');
      
      
    signUpButton.addEventListener('click', () => {
        modal_signup.classList.add('is-active');
    });
      
    closeSignupBtn.addEventListener('click', () => {
        modal_signup.classList.remove('is-active');
    })

}

// modal signin
const signInButton = document.querySelector('#signin');

if(signInButton) {
    const modal_signin = document.querySelector('#modal-signin');
    const closeSigninBtn = document.querySelector('#close-signin');


    signInButton.addEventListener('click', () => {
        modal_signin.classList.add('is-active');
    });


    closeSigninBtn.addEventListener('click', () => {
        modal_signin.classList.remove('is-active');
    })

}

function RegisterUser() {
    firstname = document.querySelector("#firstname");
    lastname = document.querySelector("#lastname");
    username = document.querySelector("#username");
    password = document.querySelector("#password");

    button_register = document.querySelector("#register_user");

    button_register.addEventListener('click', () => {
    
        data = {
            'firstname': firstname.value,
            'lastname': lastname.value,
            'username': username.value,
            'password': password.value
        }
    
        console.log(data);
        let h = new Headers();
        h.append('content-type', 'application-json');
    
    
        let options = {
            method: 'POST',
            mode: 'cors',
            header: h,
            body: JSON.stringify(data)
            
        }
    
        url = 'http://localhost:5000/register/';
    
        req = new Request(url, options);
    
        fetch(req)
        .then((response) => {
            if(response.ok) {
                return response.json();
            } else {
                throw new Error();
            }
        })
        .then((data) => {
            console.log(data);
        })
        .catch((err) => {
            console.log("Error:", err);
        })
    });

}


function CleanForm() {
    document.querySelector("#firstname").value = "";
    document.querySelector("#lastname").value = "";
    document.querySelector("#username").value = "";
    document.querySelector("#password").value = "";

    return false

}


// execute register_user
btn_register_user = document.querySelector("#register_user");
if(btn_register_user) {
    console.log(btn_register_user);
    btn_register_user.addEventListener('click', RegisterUser());
    CleanForm();
}


// log a user
function LoginUser() {
    login_username = document.querySelector("#login_username");
    login_password = document.querySelector("#login_password");

    button_login = document.querySelector("#login_user");

    button_login.addEventListener('click', () => {
    
        data = {
            'username': login_username.value,
            'password': login_password.value
        }
    
        let h = new Headers();
        h.append('content-type', 'application-json');
    
    
        let options = {
            method: 'POST',
            mode: 'cors',
            header: h,
            body: JSON.stringify(data)
            
        }
    
        url = 'http://localhost:5000/login/';
    
        req = new Request(url, options);
    
        fetch(req)
        .then((response) => {
            if(response.ok) {
                return response.json();
            } else {
                throw new Error();
            }
        })
        .then((data) => {
            data_json = JSON.parse(data);
            // get access and refresh token for login endpoint
            access_token = data_json['access_token'];
            refresh_token = data_json['refresh_token'];
            // set access and refresh token in session storage 
            localStorage.setItem('access_token', access_token);
            localStorage.setItem('refresh_token', refresh_token);
        })
        .catch((err) => {
            console.log("Error:", err);
        })
    });
}

// execute login_user
btn_login_user = document.querySelector("#login_user");
if(btn_login_user) {
    console.log(btn_login_user);
    btn_login_user.addEventListener('click', LoginUser());
}



