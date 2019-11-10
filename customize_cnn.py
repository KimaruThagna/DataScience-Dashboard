from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Dropout, Flatten, Dense
from keras.utils import to_categorical
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

# generating CNN
st.subheader('Building your Custom CNN')
st.text('Default Kernel size is the suggested 3X3')
model = Sequential()
activation_1 = st.selectbox('Activation function for first layer: ', ['relu', 'tanh', 'softmax'])

model.add(Conv2D(32,kernel_size=(3,3),activation=activation_1,input_shape=(32,32,3)))
model.add(MaxPool2D(pool_size=(2,2)))

if st.checkbox('Add hidden Conv2D layer?'):
    activation_h = st.selectbox('Activation function for hidden layer: ', ['relu', 'tanh', 'softmax'])
    model.add(Conv2D(64, kernel_size=(3, 3), activation=activation_h, input_shape=(32, 32, 3)))
    model.add(MaxPool2D(pool_size=(2, 2)))

if st.checkbox('Add a drop layer?'):
    drop1=st.selectbox('Select dropout Rate', [0.1, 0.25, 0.5])
    model.add(Dropout(drop1))
model.add(Flatten())
activation_2 = st.selectbox('Activation function for Dense layer: ', ['relu', 'tanh', 'softmax'])
model.add(Dense(1024,activation=activation_2))
activation_3 = st.selectbox('Activation function for Output layer: ', ['relu', 'tanh', 'softmax'])
model.add(Dense(10,activation=activation_3))

# model compiling
model.compile(loss=loss_function, optimizer=optimizer, metrics=['accuracy'])
if st.checkbox('Fit model'):
    history = model.fit(x_train[0:1000]/255.0, to_categorical(y_train[0:1000]),
         batch_size=batch_size,
         shuffle=True,
         epochs=epochs,
         validation_data=(x_test[0:1000]/255.0, to_categorical(y_test[0:1000]))
         )

    # Plot training & validation accuracy values
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    st.pyplot()
predictions = model.predict(x_test / 255.0)
scores = model.evaluate(x_test / 255.0, to_categorical(y_test))

st.write(f'loss: {round(scores[0], 2)}')
st.write(f'accuracy: {round(100 * scores[1], 2)}%')