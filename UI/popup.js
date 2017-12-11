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
  // Change text on extension toggle
  document.getElementById('onoff').addEventListener('click', changeText);

  // Refresh page on extension toggle
  document.getElementById('onoff').addEventListener('click', function() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.tabs.update(tabs[0].id, {url: tabs[0].url});
    });
  });

  var toggle = false;
  document.getElementById('onoff').addEventListener('click', function() {
    console.log('here');
    toggle = ! toggle;
    if (toggle) {
      // Script to block spoilers
      chrome.tabs.executeScript(null, {
        file: "bg_script.js"
      }, function() {}
      );
    }
    else {
      chrome.tabs.executeScript(null, {code: "console.log('off');"});
    }
  });
  
});

