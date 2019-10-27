import streamlit as st
import math
import pandas as pd
from matplotlib import pyplot as plt

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
fig = plt.scatter(filtered_df, y='Percent')
# Plot!
'''
### Visualization of selected Counties
'''
st.plotly_chart(fig)