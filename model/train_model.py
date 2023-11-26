from tensorflow import keras
from keras.layers import Dense,Flatten
from keras.datasets import mnist

import matplotlib.pyplot as plt

# Training dataset
(x_train,y_train),(x_test,y_test) = mnist.load_data()
x_train = x_train / 255
x_test = x_test / 255


# Model initialization 
model = keras.Sequential()

model.add(Flatten())
model.add(Dense(units=64,activation="relu"))
model.add(Dense(units=32,activation="relu"))
model.add(Dense(units=10,activation="softmax"))

model.compile(optimizer=keras.optimizers.Adam(0.001),loss="sparse_categorical_crossentropy",metrics=['accuracy'])

# Model training
history = model.fit(x_train,y_train,epochs=5,batch_size=32,verbose=True,validation_data=(x_test,y_test))


# Stats outputs
plt.subplot(121)
plt.plot(history.history['loss'], "r")
plt.xlabel("Кросс-энтропия")

plt.subplot(122)
plt.plot(history.history['accuracy'], "g")
plt.xlabel("Метрика точности")

plt.suptitle("Статистика")
plt.show()

# Saving model
model.save("model.keras")