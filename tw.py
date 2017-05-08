"""TODO:
ver lo de los truncated

"""

import tweepy #https://github.com/tweepy/tweepy
import pytz, datetime
import os

#Obtain twitter API credentials
with open('tw.config') as g:
    cred=[x.strip() for x in g.readlines()]
    
consumer_key = cred[0]
consumer_secret = cred[1]
access_key = cred[2]
access_secret = cred[3]


#Open html file
f = open('html/tweets'+str(datetime.datetime.now())+'.html','a')

#Define constants
RETWEET=1
REPLY=2
QUOTE=3

#Open the api
api = 1

count=0


#Print all relevant atributes of the tweet structure to the html file
def print_tweet(tweet, special=0, else1=0, else2=0):
    #We use text as a buffer to store all the relevant information, depending if its a normal tweet, rt, etc
    text="<a class='tweet' id='"+tweet.id_str+"' href='https://twitter.com/"+tweet.user.screen_name+"/status/"+tweet.id_str+"'>\n"
    
    if special==RETWEET:
        text+="\t<img src='imgs/rt.svg'>\n"
        text+="\t<h5>"+else1.name+"(@"+else1.screen_name+") Retweeted:</h5><br>\n"
    elif special==REPLY:
        text+="\t<a href='https://twitter.com/"+else2+"/status/"+else1+"'>In reply to "+else2+"</a><br>\n"
    
    text+="\t<img src='"+tweet.user.profile_image_url+"'  class='profile_photo'>\n"
    text+="\t\t<a href='https://twitter.com/"+tweet.user.screen_name+"'>"+tweet.user.name+"</a>\n"
    if tweet.user.verified:
        text+="\t\t<img src='https://ton.twitter.com/hc_assets/1307051244_737.png' width='23' height='23'>\n"
    text+="\t\t<h1>@"+tweet.user.screen_name+"</h1>\n"
    text+="\t\t<h2>" + pytz.utc.localize(tweet.created_at, is_dst=None).astimezone(pytz.timezone('Europe/Madrid')).strftime('%Y-%m-%d %H:%M:%S') + "</h2><br>\n"
    
    text+="\t<h3><pre>"+tweet.full_text+"</pre></h3><br>\n"
    
    if special==QUOTE:
        text+="\t\t<a class='tweet' id='"+else1[u'id_str']+"' href='https://twitter.com/"+else1[u'user'][u'screen_name']+"/status/"+else1[u'id_str']+"'>\n"
        text+="\t\t\t<h1>"+else1[u'user'][u'name']+"</h1>\n"
        text+="\t\t\t<h1>@"+else1[u'user'][u'screen_name']+"</h1>\n"
        text+="\t\t\t<h3>"+else1[u'full_text']+"</h3>\n"
        text+="\t\t</a>"
    
    if tweet.retweeted:
        text+="\t<img src='imgs/rted.svg'>\n"
    else:
        text+="\t<img src='imgs/rt.svg'>\n"
    text+="\t\t<h4>"+str(tweet.retweet_count)+"</h4>\n"
    
    if tweet.favorited:
        text+="\t<img src='imgs/faved.svg'>\n"
    else:
        text+="\t<img src='imgs/fav.svg'>\n"
    text+="\t\t<h4>"+str(tweet.favorite_count)+"</h4>\n"
    
    text+="</a>\n\n"
    
    #We wrtie the buffer to the file
    f.write(text.encode('utf-8'))
 

def get_all_tweets():
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #Authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    global api
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.home_timeline(count=200,tweet_mode='extended')
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.home_timeline(count=200,max_id=oldest,tweet_mode='extended')
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print "...%s tweets downloaded so far" % (len(alltweets))
    
    #We write the css link at the beginning of the htlm file 
    f.write('<link type="text/css" rel="stylesheet" href="css.css">\n\n'.encode('utf-8'))
    
    #We filter the tweets by their type and print them on the html file
    for tweet in reversed(alltweets):
        try:
            if hasattr(tweet, 'retweeted_status'):
                print_tweet(tweet.retweeted_status,RETWEET,tweet.user)
            elif tweet.in_reply_to_status_id_str!=None:
                print_tweet(tweet,REPLY,tweet.in_reply_to_status_id_str,tweet.in_reply_to_screen_name)
            elif tweet.is_quote_status:
                try:
                    print_tweet(tweet,QUOTE,tweet.quoted_status)
                except AttributeError:
                    print_tweet(tweet)
            else:
                if tweet.truncated:
                    print_tweet(api.get_status(tweet.id))
                else:
                    print_tweet(tweet)
        except AttributeError:
            print "Check "+tweet.id_str+" , there may be an error"


if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets()
