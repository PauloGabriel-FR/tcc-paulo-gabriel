import tensorflow as tf 
import numpy as np
from keras.layers import Flatten, Input,Dense,Dropout
from keras.models import Model
import keras
from keras.layers.merge import concatenate
from keras.utils import plot_model
from processandoentradas import getVariabels
IMAGE_SHAPE = (224,224,3)
COLUNA_SHAPE = (1,4,1)


def Alexnet():
    imagem = Input(shape=IMAGE_SHAPE)
    # 1st Convolutional Layer
    X = keras.layers.Conv2D(filters=96, kernel_size=(11,11), strides=(4,4), padding='valid',activation='relu')(imagem)
    # Pooling 
    X = keras.layers.MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid')(X)
    # Batch Normalisation before passing it to the next layer
    X = keras.layers.BatchNormalization()(X)

    # 2nd Convolutional Layer
    X = keras.layers.Conv2D(filters=256, kernel_size=(11,11), strides=(1,1), padding='valid',activation='relu')(X)
    
    # Pooling
    X = keras.layers.MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid')(X)
    # Batch Normalisation
    X = keras.layers.BatchNormalization()(X)

    # 3rd Convolutional Layer
    X = keras.layers.Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid',activation='relu')(X)
    
    # Batch Normalisation
    X = keras.layers.BatchNormalization()(X)

    # 4th Convolutional Layer
    X = keras.layers.Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid',activation='relu')(X)

    # Batch Normalisation
    X = keras.layers.BatchNormalization()(X)

    # 5th Convolutional Layer
    X = keras.layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding='valid',activation='relu')(X)
 
    # Pooling
    X = keras.layers.MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid')(X)
    # Batch Normalisation
    X = keras.layers.BatchNormalization()(X)
    
    flat1 = Flatten()(X)
    
    vetorc = Input(shape=COLUNA_SHAPE)
    flat2 = Flatten()(vetorc)
    
    merge = concatenate([flat1, flat2])
    
   
    hidden1 = Dense(4096, activation='relu')(merge)
    hidden1 = Dropout(0.5)(hidden1)
    hidden1 = keras.layers.BatchNormalization()(hidden1)
    
    hidden2 = Dense(4096, activation='relu')(hidden1)
    hidden2 = Dropout(0.5)(hidden2)
    hidden2 = keras.layers.BatchNormalization()(hidden2)
    
    hidden3 = Dense(1000, activation='relu')(hidden2)
    hidden3 = Dropout(0.5)(hidden3)
    hidden3 = keras.layers.BatchNormalization()(hidden3)
    
    output = Dense(5, activation='softmax')(hidden3)
    model = Model(inputs=[imagem, vetorc], outputs=output)
    return model

model = Alexnet()
tensorboard = keras.callbacks.TensorBoard(log_dir="logs/sad")
model.compile(optimizer="Adadelta", loss='categorical_crossentropy',metrics=['accuracy'])
Imagemcompleta,colunacompleta, saidacompleta = getVariabels()
model.fit(x=[Imagemcompleta,colunacompleta], y=saidacompleta, batch_size=16, epochs=5, callbacks = [tensorboard], verbose=1, \
    validation_split=0.3, shuffle=True)