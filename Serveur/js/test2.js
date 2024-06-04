// Page de destination
var parametres = new URLSearchParams(window.location.search);
var valeurRecue = parametres.get("valeur");
console.log("Valeur reçue : " + valeurRecue);