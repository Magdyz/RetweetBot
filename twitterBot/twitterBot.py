import tweepy
import time
from random import randrange, choice

# Authentication for user to use Twitter Api. This is used to import the credentials from auth file that exists in the same folder

def authTwitter():
    from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret)

# defining variables to be used in the Authentication process
    
    consumer_key = consumer_key
    consumer_secret = consumer_secret
    access_token = access_token
    access_token_secret = access_token_secret
    
# authentication using tweepy.OAuthHandler() - please check Tweepy documentation for more details

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth, wait_on_rate_limit = True)

# defining a function with the keywords that want to be used for topics to be retweeted. You can use a sentence, a word or more than one word 
# like in the example below. choice() function is used to return a random item from listOfWords

def searchWord():
    listOfWords = ['Check out this item','new art','art+NFT','etherium+NFT','new nft art','my latest art']
    return choice(listOfWords)

# a variable for date that could be custumised or maybe programed to used a dynamic date for the day. In this case it's a fixed date

date = "2022-03-03"

# main funtion that runs all the time until a condition is met

while True:
    api = authTwitter()

# an example of request that has a query that retweets a random post that contains one input from the list in function searchWords() without any replies or
# retweets and must contain an image with the date mentioned above this could be done for a random number of times betweek 1 - 5 with a random rest (time.sleep())
# All the random numbers could be changed but be aware that Twitter hates constent posting so make sure keep random patterns and rests

    for tweet in tweepy.Cursor(api.search_tweets,q=(f"{searchWord()} -filter:retweets -filter:replies has:images"),lang="en",since_id=date).items(randrange(5)):
        tweet.retweet()
        print (tweet.created_at, tweet.text, f'\n Retweeted next retweet in {randomise(10)}, search term {searchWord()}')
        time.sleep(randrange(10))

    print('end loop 1')

# another example but for liking a post with same filters like the one mentioned above

    for tweet in tweepy.Cursor(api.search_tweets,q=(f"{searchWord()} -filter:retweets -filter:replies has:images"),lang="en",since_id=date).items(randrange(5)):
        tweet.retweet()
        print(tweet.created_at, tweet.text, f'liked next action in {randrange(60)}, search term {searchWord()}')        
        time.sleep(randrange(60))

    print('end loop 2')

## An option to update status and could be designed in the same way as the searchWords with a list of statuses or use a file and open() readlines() to
## update status 

#    api.update_status('What a beautiful day today! What are you working on?')
#    print('status updated')
#    time.sleep(randrange(10))
#    print('end of loop!')
