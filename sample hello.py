import streamlit as st
import math
x = st.slider('x')
st.write(x, 'factorial is', math.factorial(x))