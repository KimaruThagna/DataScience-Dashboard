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

# train test split
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# boolean on whether to show images
if st.checkbox('Show images sizes'):
    st.write(f'X Train Shape: {x_train.shape}')
    st.write(f'X Test Shape: {x_test.shape}')
    st.write(f'Y Train Shape: {y_train.shape}')
    st.write(f'Y Test Shape: {y_test.shape}')

# display some random images
classes = ['Sneaker', 'Coat', 'Dress', 'Shirt', 'Sandal']
st.subheader('Inspect dataset')
if st.checkbox('Display random image from the train set'):
    num = np.random.randint(0, x_train.shape[0])
    img = x_train[num]
    st.image(img, caption=classes[y_train[num][0]], use_column_width=True)

# interactive hyperparameter settings
st.subheader('Set some hyperparameters for model tuning')
batch_size = st.selectbox('Select batch size', [32, 64, 128, 256])
epochs=st.selectbox('Select number of epochs', [10, 25, 50])
loss_function = st.selectbox('Loss function', ['mean_squared_error', 'mean_absolute_error', 'categorical_crossentropy'])
optimizer = st.selectbox('Optimizer', ['SGD', 'RMSprop', 'Adam'])