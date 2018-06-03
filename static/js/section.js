/* Recebe a url e retorna os parametros */
function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

var submit = getParameterByName('submit');

/* Faz rolagem para sessão de locais no html */
if (submit=="locais"){
	var scrolldown = document.getElementById("locais");
	scrolldown.scrollIntoView();
}
