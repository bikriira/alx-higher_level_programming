// ----------Uncoment for decoded results-----------
// function decodeEntities(encodedString) {
//     var textarea = document.createElement('textarea');
//     textarea.innerHTML = encodedString;
//     return textarea.value;
// }
$(document).ready(function () {
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (data) => {
      $('DIV#hello').text(data.hello);
      // $('DIV#hello').text(decodeEntities(data.hello))
    });
  });
});
