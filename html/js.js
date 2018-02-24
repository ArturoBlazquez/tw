setTimeout(function(){
        $("twitterwidget").css("margin","-1px auto");
        $("twitterwidget").css("width","550px");
        
        arr=$(".rtText")
        for ( var i = 0, l = arr.length; i < l; i++ ) {
            $(".rtText + twitterwidget /deep/ .EmbeddedTweet-tweet")[0].prepend(arr[ i ]);
        }
        $(".rtText").remove()

        $("twitterwidget /deep/ .rtText").css("margin-top", "-5px")
        $("twitterwidget /deep/ .rtText").css("margin-bottom", "10px")

        $("twitterwidget /deep/ .rtText img").css("width", "19px")
        $("twitterwidget /deep/ .rtText img").css("display", "inline")
        $("twitterwidget /deep/ .rtText img").css("float", "left")
        $("twitterwidget /deep/ .rtText img").css("padding-right", "7px")

        $("twitterwidget /deep/ .rtText h5").css("display", "inline")
        $("twitterwidget /deep/ .rtText h5").css("color", "#657786")

        $("twitterwidget /deep/ .rtText a").css("color", "#657786")
    }, 5000);

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
