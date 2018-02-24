/*Para el movil*/
if(window.innerWidth<1000){
    setTimeout(function(){
        $("iframe").css("margin","-1px 0");
        $("iframe").css("width","350px");

        arr=$(".rtText")
        for ( var i = 0, l = arr.length; i < l; i++ ) {
            if($(".rtText + iframe")[0].contentWindow.document.getElementsByClassName("EmbeddedTweet-Tweet")[0]!=undefined){
                $(".rtText + iframe")[0].contentWindow.document.getElementsByClassName("EmbeddedTweet-Tweet")[0].prepend(arr[ i ]);
            }else{
                $(".rtText + iframe")[0].remove()
            }
        }
        $(".rtText").remove()

        for ( var i = 0, l = $("iframe").length-1; i < l; i++ ) {
            rtText=$("iframe")[i].contentWindow.document.getElementsByClassName("rtText")[0]
            
            if(rtText!=undefined){
                $(rtText).css("margin-top", "-5px")
                $(rtText).css("margin-bottom", "10px")

                
                $(rtText.getElementsByTagName("img")[0]).css("width", "19px")
                $(rtText.getElementsByTagName("img")[0]).css("display", "inline")
                $(rtText.getElementsByTagName("img")[0]).css("float", "left")
                $(rtText.getElementsByTagName("img")[0]).css("padding-right", "7px")

                $(rtText.getElementsByTagName("h5")[0]).css("display", "inline")
                $(rtText.getElementsByTagName("h5")[0]).css("color", "#657786")

                $(rtText.getElementsByTagName("a")[0]).css("color", "#657786")
            }
        }
    }, 10000);
}/*Para el ordenador*/
else{
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
    }, 7000);
}

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
