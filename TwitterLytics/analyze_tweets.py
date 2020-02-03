import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time
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
api = crea
# As long as the query is valid (not empty or equal to '#')...
if query != '' and query != '#':
    with st.spinner(f'Searching for and analyzing {query}...'):
        # Get English tweets from the past 4 weeks
        tweets = api.search(q="Python", lang="en", rpp=10):
        # Initialize empty dataframe
        tweet_data = pd.DataFrame({
            'tweet': [],
            'sentiment': []
        })

        # Add data for each tweet
        for tweet in tweets[:10]:
            if tweet.text in ('', ' '): # empty tweet
                continue
            # Make predictions
            sentiment = sentiment_analyzer_scores(tweet.text)
            sentiment_socres = f'Neutral score: {sentiment["neu"]}\n' \
                               f'Positive score: {sentiment["pos"]}\n' \
                               f'Negative score: {sentiment["neg"]}\n' \

            # Append new data
            tweet_data = tweet_data.append({'tweet': tweet.text, 'predicted-sentiment': sentiment_socres}, ignore_index=True)
