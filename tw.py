import os
import time
from codecs import open

import tweepy

from get_configs import get_configs


# Returns the html text to append
def get_html(tweet, is_rt=False, retweet=None):
    if is_rt:
        addr = "https://twitter.com/" + retweet.user.screen_name + "/status/" + retweet.id_str
        ret = "\t<div class='rtText'><img src='imgs/rt.svg'><h5><a href='https://twitter.com/" + tweet.user.screen_name + "'>" + tweet.user.name + "</a> Retweeted:</h5></div>\n"
        return ret + "\t\t<blockquote class='twitter-tweet tw-align-center'>" + addr + "<a href='" + addr + "'></a></blockquote>\n"
    else:
        addr = "https://twitter.com/" + tweet.user.screen_name + "/status/" + tweet.id_str
        return "\t<blockquote class='twitter-tweet tw-align-center'>" + addr + "<a href='" + addr + "'></a></blockquote>\n"


# Twitter only allows access to a users most recent 3240 tweets with this method
def get_all_tweets():
    # Authorize twitter, initialize tweepy
    consumer_key, consumer_secret, access_key, access_secret, public_address = get_configs(return_length=5)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    now = time.strftime("%Y-%m-%d_%H:%M")
    
    all_tweets = []
    
    # Make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.home_timeline(count=200, tweet_mode='extended')
    
    # Save most recent tweets and oldest id
    all_tweets.extend(new_tweets)
    oldest = all_tweets[-1].id - 1
    
    # Keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))
        
        # All subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.home_timeline(count=200, max_id=oldest, tweet_mode='extended')
        
        # Save most recent tweets and oldest id
        all_tweets.extend(new_tweets)
        oldest = all_tweets[-1].id - 1
        
        print("...%s tweets downloaded so far" % (len(all_tweets)))
    
    # Write the tweets in lots of 150 so that the widget doesn't get bugged
    for i in range(0, len(all_tweets), 150):
        
        # Write the css and js links at the beginning of the html file
        text = '<link type="text/css" rel="stylesheet" href="css.css">'
        text += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>'
        text += '<script src="js.js"></script>\n\n'
        
        # Print the tweets on the html file
        for tweet in all_tweets[i:i + 160]:
            if hasattr(tweet, 'retweeted_status'):
                text += get_html(tweet, True, tweet.retweeted_status)
            else:
                text += get_html(tweet)
        
        # Add twitter js and save the html file
        text += '\n\n<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
        
        actual_path = os.path.dirname(os.path.abspath(__file__)) + '/'
        with open(actual_path + 'html/tweets_' + now + "_(" + str(i) + ")" + '.html', 'a', 'utf-8') as f_private:
            f_private.write(text)
        
        if public_address:
            with open(public_address + 'tweets_' + now + "_(" + str(i) + ")" + '.html', 'a', 'utf-8') as f_public:
                f_public.write(text)


if __name__ == '__main__':
    get_all_tweets()

# TODO: intentar encontrar una manera de no tener que hacer mil archivos
