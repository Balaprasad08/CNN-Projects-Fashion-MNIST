# -*- coding: utf-8 -*-
"""CNN Using Fashion MNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rbd1R0pJE6QaDwK5iSA2Yyp8lFVyKOme
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import keras

"""Fashion MNIST Clothing Classification
The Fashion-MNIST dataset is proposed as a more challenging replacement dataset for the MNIST dataset.

It is a dataset comprised of 60,000 small square 28×28 pixel grayscale images of items of 10 types of clothing, such as shoes, t-shirts, dresses, and more. The mapping of all 0-9 integers to class labels is listed below.

0: T-shirt/top
1: Trouser
2: Pullover
3: Dress
4: Coat
5: Sandal
6: Shirt
7: Sneaker
8: Bag
9: Ankle boot
"""

from keras.datasets import fashion_mnist

(X_train,y_train),(X_test,y_test)=fashion_mnist.load_data()

X_train.shape,X_test.shape

y_train.shape,y_test.shape

# Data Visualization
for i in range(9):
  plt.subplot(330+1+i)
  plt.imshow(X_train[i],cmap='gray')
plt.show()

for i in range(9):
  plt.subplot(330+1+i)
  plt.imshow(X_test[i],cmap='gray')

y_test[0:9]

# Reshape Dataset to have a Single Channel
X_train=X_train.reshape(-1,28,28,1)
X_test=X_test.reshape(-1,28,28,1)

# Convert integers to float
from keras.utils import to_categorical
X_train=X_train.astype('float')
X_test=X_test.astype('float')

# Normalization Between 0-1 format
X_train=X_train/255
X_test=X_test/255

y_train_ohe=to_categorical(y_train)
y_test_ohe=to_categorical(y_test)

# import Keras Important Libraries
import keras
from keras.models import Sequential
from keras.layers import Dense,Dropout,Conv2D,MaxPooling2D,Flatten,Activation

# Initialising the CNN
model=Sequential()

# Step 1 - Convolution Layer
model.add(Conv2D(64, (3,3),input_shape=(28,28,1),activation='relu'))

# Step 2 - Pooling Layer
model.add(MaxPooling2D(pool_size=(2,2)))

# add Second Convolution Layer
model.add(Conv2D(64, (3,3),activation='relu'))

# add Second Pooling Layer
model.add(MaxPooling2D(pool_size=(2,2)))

# Step 3 - Flattening
model.add(Flatten())

# Step 4 - Full connection Layer
model.add(Dense(64,activation='relu'))
model.add(Dense(10,activation='softmax'))

# Compiling the CNN
model.compile(optimizer='Adam',loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(X_train,y_train_ohe,batch_size=10,epochs=10)

# test_loss,test,accuracy=model.evaluate(X_test,y_test_ohe,batch_size=1,)

prediction=model.predict(X_test)

print(np.argmax(np.round(prediction[2])))

plt.imshow(X_test[2].reshape(28,28),cmap='gray')
plt.show()

print(np.argmax(np.round(prediction[250])))

plt.imshow(X_test[250].reshape(28,28),cmap='gray')
plt.show()

