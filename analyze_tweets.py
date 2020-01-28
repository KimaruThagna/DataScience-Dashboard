import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time
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