let isPhone = window.innerWidth < 1000;

setTimeout(function() {
  var button = document.createElement("BUTTON");
  button.innerHTML = "Formatear";
  document.body.prepend(button);
  $("body > button").css({ "height": "200px", "width": "600px", "font-size": "50px" });

  if (isPhone) {
    button.addEventListener("click", function() {
      $("body").css({ "margin": "0px 0px 10px 545px", "transform": "scale(3.5)", "overflow-x": "hidden" });
      $(".twitter-tweet.twitter-tweet-rendered").css({ "margin": "-1px 5px", "width": "400px", "align": "right" });
      $("body").css("margin-top", -$(".twitter-tweet.twitter-tweet-rendered").position().top);
      window.scrollTo(0, document.body.scrollHeight);
    });
  } else {
    button.addEventListener("click", function() {
      $(".twitter-tweet.twitter-tweet-rendered").css({ "margin": "0 auto -1px" });
    });
  }
}, 100);

window.twttr = (function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0],
    t = window.twttr || {};
  if (d.getElementById(id)) return t;
  js = d.createElement(s);
  js.id = id;
  js.src = "https://platform.twitter.com/widgets.js";
  fjs.parentNode.insertBefore(js, fjs);

  t._e = [];
  t.ready = function(f) {
    t._e.push(f);
  };

  return t;
}(document, "script", "twitter-wjs"));
