$(document).ready(function () {
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();
    translate(lang);
  });
  $('INPUT#language_code').keypress((e) => {
    const lang = $('INPUT#language_code').val();
    if (e.keyCode == 13) translate(lang);
  });

  function translate (lang) {
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (data) => {
      $('DIV#hello').text(data.hello);
    });
  }
});
