/*
1. On/Off functionality (only work when on, reload page on toggle)
2. 
*/


console.log(window.location);
scrapeTweets();
function scrapeTweets() {
    var tweets_query = $('.TweetTextSize');
    console.log(tweets_query);

    var data = new FormData();

    var tweet_data = new Array(tweets_query.length);
    for (var i = 0; i < tweet_data.length; i++) {
        
        var key = "post" + i; 
        tweet_data[i] = tweets_query[i].innerText;
        data.append(key, tweet_data[i]);
    }

    console.log(tweet_data);

    var xhr = createCORSRequest('POST', 'https://localhost:5000/classify');
    if (!xhr) {
        console.log('CORS not suppoerted');
    }

    xhr.onload = function() {
        var response_labels = xhr.responseText.split(',');
        console.log(response_labels);
        for (var i = 0; i < response_labels.length; i++) {
            if (response_labels[i] == "1") {
                tweets_query[i].style.visibility = "hidden";
            }
        }

    }
    xhr.onerror = function() {
        console.log('coudlnt load');
    }
    xhr.send(data);
}

function createCORSRequest(method, url) {
    var xhr = new XMLHttpRequest();

    if ('withCredentials' in xhr) {
        xhr.open(method, url, true);
    }
    else {
        console.log('OH NO');
    }

    return xhr;
}