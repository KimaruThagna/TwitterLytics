from word_freq_analysis import *

# explore bigrams/co-occuring words

# Create list of lists containing bigrams in tweets
terms_bigram = [list(bigrams(tweet)) for tweet in tweets_nsw_nc]

# View bigrams for the first tweet
print(f' co-occuring words{terms_bigram[0]}')

# top 20 most commonly used bi-grams
# Flatten list of bigrams in clean tweets
bigrams = list(itertools.chain(*terms_bigram))

# Create counter of words in clean bigrams
bigram_counts = collections.Counter(bigrams)

print(f'Most common bi-grams {bigram_counts.most_common(20)}')
# convert to pandas DF
bigram_df = pd.DataFrame(bigram_counts.most_common(20),
                             columns=['bigram', 'count'])
