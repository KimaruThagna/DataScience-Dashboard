import streamlit as st
import math
import pandas as pd
x = st.slider('x')
st.write(x, 'factorial is', math.factorial(x))
# exploring widgets
# text input
value = st.text_input('Enter Values of X')
st.write('The Entered value is', value)
#checkbox
df = pd.read_csv("football_data.csv")
if st.checkbox('Show dataframe'):
    st.write(df)

#selectionbox
option = st.selectbox(
    'Which Club do you like best?',
     df['Club'].unique())
st.write('You selected: ', option)

# multi selector
options = st.multiselect(
 'What are your favorite clubs?', df['Club'].unique())
st.write('You selected:', options)