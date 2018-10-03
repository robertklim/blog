var keywords_endpoint = '/api/articles/keywords/';
var search_endpoint = '/articles/search/?q=';
var autocomplete_keywords = {};

fetch(keywords_endpoint)
    .then(function (response) {
        return response.json();
    })
    .then(function (myJson) {
        for (let i=0; i < myJson.length; i++) {
            if (isNaN(parseInt(myJson[i][1]))) {
                autocomplete_keywords[myJson[i][0]] = myJson[i][1];
            } else {
                autocomplete_keywords[myJson[i][0]] = null;
            }
        }
    });

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.autocomplete');
    var options = {
        data: autocomplete_keywords,
        onAutocomplete: function (val) {
            location.href = search_endpoint + val;
        },
    }
    var instances = M.Autocomplete.init(elems, options);
});