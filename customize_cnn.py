import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import pydot_ng as pydot
import streamlit as st
from keras.datasets import fashion_mnist
st.title('Customizable Convolutional Neural Network')
st.header('Dataset: Fashion MNIST')
st.text("This page allows you to build and train a CNN for the fashion MNIST dataset via an interactive visual interface")