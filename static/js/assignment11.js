
function getUsers() {
    let id = parseInt(document.getElementById('id').value);
    fetch(`https://reqres.in/api/users/${id}`).then(
        response => response.json()
    ).then(
        response_obj => put_users_html(response_obj.data)
    ).catch(
        err=>console.log(err)
    )
}

function put_users_html(response_obj_data) {
    const curr_main = document.querySelector("main");
        while (curr_main.firstChild) {
        curr_main.removeChild(curr_main.lastChild);
    }
    const section = document.createElement('section');
    section.innerHTML = `
    <img src="${response_obj_data.avatar}" alt="Profile Picture"/>
    <div>
       ${response_obj_data.id}
       <br>
       ${response_obj_data.first_name} ${response_obj_data.last_name}
       <br>
       ${response_obj_data.email}
    </div>
    `;
    curr_main.appendChild(section);
}