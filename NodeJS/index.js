const Twit = require('twit')
const fs = require('fs');

const hashTag = "#girlPower"

var T = new Twit({
  consumer_key: "HTNc6rm4tX63VYQKWQCV40TFm",
  consumer_secret: "bAWS75kNkDMKrWvGvzoGVYrRdjrtrZk7BaPwTBcBzdpfdHr0Il",
  access_token: "969603656080330753-ucYDl5fW5aJmzT2AJIuR6wtKaa8Jf7A",
  access_token_secret: "HrI9XHNBqtQ0xxouDPqeY6OOOzLav1moLk1BgP7l29an9",
  timeout_ms: 60 * 1000,  // optional HTTP request timeout to apply to all requests.
  strictSSL: true,     // optional - requires SSL certificates to be valid.
})

T.get('search/tweets', { q: hashTag, count: 1000 }, function (err, data, response) {
  var twitsData = JSON.stringify(data.statuses);
  fs.writeFile('./output.json', twitsData, 'utf8', function () {
    console.log("Output generated successfully")
  });
})    