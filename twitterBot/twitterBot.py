import tweepy
import time
from random import randrange, choice


def authTwitter():
    from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret)
    
    consumer_key = consumer_key
    consumer_secret = consumer_secret
    access_token = access_token
    access_token_secret = access_token_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth, wait_on_rate_limit = True)

#Installation / Access to Twitter account

def searchWord():
    listOfWords = ['Check out this item on OpenSea','pixel art','art+NFT','etherium+NFT','NFTs+art','new nft art','my latest art']
    return choice(listOfWords)

while True:
    api = authTwitter()
    searchPerson = "-filter:from:elonmusk"

    for tweet in tweepy.Cursor(api.search_tweets,q=(f"{searchWord()} -filter:retweets -filter:replies has:images"),lang="en",since_id="2022-03-03").items(randrange(5)):
        tweet.retweet()
        print (tweet.created_at, tweet.text, f'\n Retweeted next retweet in {randomise(10)}, search term {searchWord()}')
        time.sleep(randrange(10))

    print('end loop 1')

    for tweet in tweepy.Cursor(api.search_tweets,q=(f"{searchWord()} -filter:retweets -filter:replies has:images"),lang="en",since_id="2022-03-03").items(randrange(5)):
        tweet.retweet()
        print(tweet.created_at, tweet.text, f'liked next action in {randrange(60)}, search term {searchWord()}')        
        time.sleep(randrange(60))

    print('end loop 2')

    for tweet in tweepy.Cursor(api.search_tweets,q=searchPerson,lang="en",since_id="2022-03-03").items(randrange(2)):
        tweet.retweet()
        print(tweet.created_at, tweet.text, f'\n Retweeted next action in {randomise(60)}, search term {searchWord()}')        
        time.sleep(randrange(60))    
    print('end loop 3')


#    api.update_status('What a beautiful day today! What are you working on?')
#    print('status updated')
#    time.sleep(randrange(10))
#    print('end of loop!')
