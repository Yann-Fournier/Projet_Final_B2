var divTest = document.getElementById("test");
var header = {
    'Authorization': `Bearer `
}

// var truc = [{"Id":0,"Is_Admin":true}]
// divTest.innerText = truc;

// fetch("http://localhost:8080/user?user_id=2")
//     .then((response) =>  {
//         return response.json();
//     }).then((json) => {
//         // localStorage.setItem('Next GP', JSON.stringify(json));
//         // divTest.innerHTML = json.keys();
//         console.log(json[0]);
//         divTest.innerHTML = json[0].Email;
//     });

// Page d'origine
var bouton = document.getElementById("truc");

bouton.addEventListener('click', function() {
    var valeur = bouton.value;
    console.log(valeur);
    window.location.href = "test2.html?Id=" + encodeURIComponent(valeur);
});


