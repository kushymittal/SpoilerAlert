function changeText() {
  var button = document.getElementById('onoff');
  var textTag = document.getElementById('ext_status');

  if (button.checked) {
    textTag.innerHTML = "SpoilerAlert is currently enabled.";
  }
  else {
    textTag.innerHTML = "SpoilerAlert is currently disabled.";
  }
}

function getCurrentTabURL() {
  var queryInfo = {
    active: true,
    currentWindow: true
  }

  chrome.tabs.query(queryInfo, (tabs) => {
    var tab = tabs[0];
    var url = tab.url;

    console.log(url);
  });
}

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('onoff').addEventListener('click', changeText);
  
  chrome.tabs.executeScript(null, {
    file: "bg_script.js"
  }, function(results) {
    console.log('finished executing' + results);
  });
})

