/*
1. Select post data based on current domain
2. Send data to endpoint using a post request
3. Get response, block all posts that are spoilers
*/


console.log(window.location);
scrapeTweets();
function scrapeTweets() {
    var tweets_query = $('.TweetTextSize');
    console.log(tweets_query);

    var tweet_data = new Array(tweets_query.length);
    for (var i = 0; i < tweet_data.length; i++) {
        tweet_data[i] = tweets_query[i].innerText;
    }

    console.log(tweet_data);

    /*
    var data = new FormData();
    data.append('ok', 'John SNow is king in the north');

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://localhost:5000/classify'), true;
    xhr.onload = function () {
        console.log(this.responseText);
    }
    xhr.send(data)*/

    var xhr = createCORSRequest('GET', 'https://localhost:5000/');
    if (!xhr) {
        console.log('CORS not suppoerted');
    }

    xhr.onload = function() {
        console.log('response: ' + xhr.responseText + 'ended');
    }
    xhr.onerror = function() {
        console.log('coudlnt load');
    }
    xhr.send();
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