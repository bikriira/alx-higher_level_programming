$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data, status) => {
    $('DIV#character').text(data.name);
  });
});
