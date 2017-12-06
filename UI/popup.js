function changeText() {
  console.log('HERE')
  var button = document.getElementById('onoff');
  var textTag = document.getElementById('ext_status');

  if (button.checked) {
    textTag.innerHTML = "SpoilerAlert is currently enabled.";
  }
  else {
    textTag.innerHTML = "SpoilerAlert is currently disabled.";
  }
}

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('onoff').addEventListener('click', changeText);
})