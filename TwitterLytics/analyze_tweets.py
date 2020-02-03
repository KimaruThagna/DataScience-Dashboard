import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time
from TwitterLytics.config.config import create_api
import datetime as dt
import pandas as pd

st.title('Sentiment Analysis')
st.header('Senti-Tweet')
st.text("Emotion AI. What was the twitter user feeling?")

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence) # obtain polarity index of given sentence.
    # produces the index of the -ve, +ve, neutral and compound sentiment
    # the compound score is a sum of all lexicon ratings normalized between -1(very negative) to 1 (very positive)
    return score

with st.spinner('Firing up the engines...'):
    time.sleep(2) # animate loading spinner

st.subheader('Single Sentence classification')
text_input = st.text_input('Sentence:')

# Make predictions
with st.spinner('Predicting...'):
    score = sentiment_analyzer_scores(text_input)

    # Show predictions
    if text_input != '':
        st.write('Prediction:')
        st.write(f'Neutral score: {score["neu"]}')
        st.write(f'Negative score: {score["neg"]}')
        st.write(f'Positive score: {score["pos"]}')
        st.write(f'Compound score: {score["compound"]}')

st.subheader('Search Twitter for Query')

# Get user input
query = st.text_input('Query:', '#')
api = create_api() # tweepy API
tweet_block = ''
tweet_data = []
# As long as the query is valid (not empty or equal to '#')...
if query != '' and query != '#':
    with st.spinner(f'Searching for and analyzing {query}...'):
        # Get English tweets from the past 4 weeks
        for tweet in  api.search(q=query, lang="en", rpp=100): # most recent 100 publicc tweets that contain the query word
            tweet_block.join(f'**{tweet.text}') # accumulate all tweets into one major string


        # Add data for each tweet
        for tweet in tweet_block.split('**')[:10]:
            if tweet in ('', ' '): # empty tweet
                continue
            # Make predictions
            sentiment = sentiment_analyzer_scores(tweet)
            sentiment_socres = f'Neutral score: {sentiment["neu"]}\n' \
                               f'Positive score: {sentiment["pos"]}\n' \
                               f'Negative score: {sentiment["neg"]}\n' \

            # Append new data
            tweet_data = tweet_data.append({'tweet': tweet, 'predicted-sentiment': sentiment_socres})
        print(tweet_data)
        # general sentiment
        general_sentiment = sentiment_analyzer_scores(tweet_block) # derive a general sentiment from all the tweets
        general_sentiment_socres = f'Neutral score: {general_sentiment["neu"]}\n' \
                           f'Positive score: {general_sentiment["pos"]}\n' \
                           f'Negative score: {general_sentiment["neg"]}\n' \
