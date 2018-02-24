import tweepy #https://github.com/tweepy/tweepy
import time
import os

actual_path = os.path.dirname(os.path.abspath(__file__))+'/'

#Obtain twitter API credentials
with open(actual_path+'tw.config') as g:
    cred=[x.strip() for x in g.readlines()]

consumer_key = cred[0]
consumer_secret = cred[1]
access_key = cred[2]
access_secret = cred[3]
public_address = cred[4]
now=time.strftime("%Y-%m-%d_%H:%M")

#Open the api
api = 1


#Returns the html text to append
def get_html(tweet, isRT=False, retweet=None):
    if isRT:
        addr="https://twitter.com/"+retweet.user.screen_name+"/status/"+retweet.id_str
        ret="\t<div class='rtText'><img src='imgs/rt.svg'><h5><a href='https://twitter.com/"+tweet.user.screen_name+"'>"+tweet.user.name+"</a> Retweeted:</h5></div>\n"
        return ret+"\t\t<blockquote class='twitter-tweet tw-align-center'>"+addr+"<a href='"+addr+"'></a></blockquote>\n"
    else:
        addr="https://twitter.com/"+tweet.user.screen_name+"/status/"+tweet.id_str
        return "\t<blockquote class='twitter-tweet tw-align-center'>"+addr+"<a href='"+addr+"'></a></blockquote>\n"
 

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
    
    #We write the tweets in lots of 150 so that the widget doesn't get bugged
    for i in range(0,len(alltweets),150):
        
        f = open(actual_path+'html/tweets_'+now+"_("+str(i)+")"+'.html','a')
        faux = open(public_address+'tweets_'+now+"_("+str(i)+")"+'.html','a')
        
        #We write the css and js links at the beginning of the html file 
        text='<link type="text/css" rel="stylesheet" href="css.css">'
        text+='<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>'
        text+='<script src="js.js"></script>\n\n'
        
        #We print the tweets on the html file
        for tweet in alltweets[i:i+160]:
            if hasattr(tweet, 'retweeted_status'):
                text+=get_html(tweet, True, tweet.retweeted_status)
            else:
                text+=get_html(tweet)
        
        #We add twitter js and save the html file
        text+='\n\n<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
        f.write(text.encode('utf-8'))
        faux.write(text.encode('utf-8'))

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets()
