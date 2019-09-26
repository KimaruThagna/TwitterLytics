import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections
import tweepy as tw
import nltk
from nltk.corpus import stopwords
import re
import networkx
from extract_tweets import api
import warnings
warnings.filterwarnings("ignore")

sns.set(font_scale=1.5)
sns.set_style("whitegrid")

search_term = "#climate+change -filter:retweets"

tweets = tw.Cursor(api.search,
                   q=search_term,
                   lang="en",
                   since='2018-11-01').items(1000)

all_tweets = [tweet.text for tweet in tweets]

print(f' Sample tweets \n {all_tweets[:5]}')

# use regular expressions to remove irrelevant urls first part of the regex removes symbols. The second part removes urls in the format
# http or https:// ((any url form))
def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

all_tweets_no_urls = [remove_url(tweet) for tweet in all_tweets]
print(f'tweets with no urls {all_tweets_no_urls[:5]}')

# Create a list of lists containing lowercase words for each tweet
words_in_tweet = [tweet.lower().split() for tweet in all_tweets_no_urls]
print(f'>>>>>>>>>>>>>>>\n{words_in_tweet[:2]}')

# List of all words across tweets
all_words_no_urls = list(itertools.chain(*words_in_tweet))

# Create counter
counts_no_urls = collections.Counter(all_words_no_urls)

print(f'>>>>>>>>15 most common words {counts_no_urls.most_common(15)}')

clean_tweets_no_urls = pd.DataFrame(counts_no_urls.most_common(15),
                             columns=['words', 'count'])

print(clean_tweets_no_urls.head())

# Download stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# View a few words from the set
print(f'View the first 10 stopwords {list(stop_words)[0:10]}')