import os
import tweepy as tw
import pandas as pd

auth = tw.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])
api = tw.API(auth, wait_on_rate_limit=True)

# Post a tweet from Python
api.update_status("Look, I'm tweeting from #Python in my #earthanalytics class! @EarthLabCU")

# Define the search term and the date_since date as variables
search_words = "#wildfires"
date_since = "2018-11-16"

new_search = search_words + " -filter:retweets" # remove retweets
new_search_2= "climate+change -filter:retweets"

'''
Sometimes you may want to remove retweets as they contain duplicate content that might skew your analysis 
if you are only looking at word frequency.
'''

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)


# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)

# who is tweeting about a certain topic and from where
users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
for item in users_locs:
    print(item)
# create a dataframe
tweet_text = pd.DataFrame(data=users_locs,
                    columns=['user', "location"])

print(f'Twitter user and location in  a pandas DF {tweet_text}')