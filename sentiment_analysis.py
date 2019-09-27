from word_freq_analysis import *

# Create textblob objects of the tweets
sentiment_objects = [TextBlob(tweet) for tweet in all_tweets_no_urls]

print(f'Sentiment polarity and tweet {sentiment_objects[0].polarity, sentiment_objects[0]}')
# create dataframe for the polarity and tweet
sentiment_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiment_objects]
sentiment_df = pd.DataFrame(sentiment_values, columns=["polarity", "tweet"])

print(f'Sentiment dataframe{sentiment_df.head()}')
# Plot histogram of the polarity values
fig, ax = plt.subplots(figsize=(8, 6))
sentiment_df.hist(bins=[-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1],
                  ax=ax,
                  color="purple")

plt.title("Sentiments from Tweets on Climate Change")
plt.show()