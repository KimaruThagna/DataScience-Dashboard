import streamlit as st
import math
import pandas as pd
from matplotlib import pyplot as plt


#df = st.cache(pd.read_csv)("football_data.csv")
# @st.cache
# def complex_func(a,b):
#     DO SOMETHING COMPLEX
# # Won't run again and again.
# complex_func(a,b)
st.header("Hello World Streamlit")
x = st.slider('x')
st.write(x, 'factorial is', math.factorial(x))
# exploring widgets
# text input
value = st.text_input('Enter Values of X')
st.write('The Entered value is', value)
#checkbox

'''
### StreamLit Dashboard Sample App
Interactive dashboard on Land under irrigation in Kenyan Counties
'''
df = pd.read_csv("datasets/land_under_Irrigation.csv")
if st.checkbox('Show dataframe'):
    st.write(df)

#selectionbox
option = st.selectbox(
    'Which County do you wish to View?',
     df['County'].unique())
st.write('You selected: ', option)

# multi selector
options = st.multiselect(
 'What are the most promising counties?', df['County'].unique())
st.write('You selected:', options)

#filter dataframe
counties = st.sidebar.multiselect('Show land under irrigation for County?', df['County'].unique())
# Filter dataframe
filtered_df = df[(df['County'].isin(counties)) ]
# write dataframe to screen
st.write(filtered_df)
# plot data
# create figure

fig = plt.scatter(data=filtered_df, x='County', y='Percent')
# Plot!
#https://towardsdatascience.com/building-machine-learning-apps-with-streamlit-667cef3ff509
'''
### Visualization of selected Counties
'''
st.pyplot(fig)