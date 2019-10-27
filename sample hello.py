import streamlit as st
import math
x = st.slider('x')
st.write(x, 'factorial is', math.factorial(x))
# exloring widgets
# text input
value = st.text_input('Enter Values of X')
st.write('The Entered value is', value)