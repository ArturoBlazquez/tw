let isPhone = window.innerWidth < 1000;

if (isPhone) {
    setTimeout(function () {
        insertRtTextIntoTweet();

        $("body").css({"margin": "0px 0px 10px 545px", "transform": "scale(3.5)"});
        $("twitter-widget").css({"margin": "-1px 5px", "width": "400px", "align": "right"});
        $("body").css("margin-top", -$("twitter-widget").position().top)
        window.scrollTo(0, document.body.scrollHeight);
    }, 10000);
} else {
    setTimeout(function () {
        insertRtTextIntoTweet();

        $("twitter-widget").css({"margin": "-1px auto", "width": "550px"});
    }, 7000);
}

function insertRtTextIntoTweet() {
    let arr = $(".rtText");
    for (let i = 0; i < arr.length; i++) {
        let tweet = $(".rtText + twitter-widget")[0].shadowRoot.querySelector(".EmbeddedTweet-tweet");
        if (tweet != null) {
            tweet.prepend(arr[i]);

            let rtText = tweet.getElementsByClassName("rtText")[0];
            $(rtText).css({"margin-top": "-5px", "margin-bottom": "10px"});

            let img = rtText.getElementsByTagName("img")[0];
            $(img).css({"width": "19px", "display": "inline", "float": "left", "padding-right": "7px"});

            let h5 = rtText.getElementsByTagName("h5")[0];
            $(h5).css({"display": "inline", "color": "#657786"});

            let a = rtText.getElementsByTagName("a")[0];
            $(a).css("color", "#657786");
        } else {
            $(".rtText + twitter-widget")[0].remove()
        }
    }
}

window.twttr = (function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0],
        t = window.twttr || {};
    if (d.getElementById(id)) return t;
    js = d.createElement(s);
    js.id = id;
    js.src = "https://platform.twitter.com/widgets.js";
    fjs.parentNode.insertBefore(js, fjs);

    t._e = [];
    t.ready = function (f) {
        t._e.push(f);
    };

    return t;
}(document, "script", "twitter-wjs"));