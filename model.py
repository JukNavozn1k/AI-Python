from tensorflow import keras
from keras.layers import Dense,Flatten
from keras.datasets import mnist
import matplotlib.pyplot as plt


class Model:
    def print_stats(self,history):
        # Stats outputs
        plt.subplot(121)
        plt.plot(history.history['loss'], "r")
        plt.xlabel("Кросс-энтропия")

        plt.subplot(122)
        plt.plot(history.history['accuracy'], "g")
        plt.xlabel("Метрика точности")

        plt.suptitle("Статистика")
        plt.show()
    def train(self,stats=False):
      
        # Training dataset
        (x_train,y_train),(x_test,y_test) = mnist.load_data()
        x_train = x_train / 255
        x_test = x_test / 255
        # Model initialization 
        self.model = keras.Sequential()

        self.model.add(Flatten())
        self.model.add(Dense(units=64,activation="relu"))
        self.model.add(Dense(units=64,activation="relu"))
        self.model.add(Dense(units=10,activation="softmax"))

        self.model.compile(optimizer=keras.optimizers.Adam(0.001),loss="sparse_categorical_crossentropy",metrics=['accuracy'])

        # Model training
        history = self.model.fit(x_train,y_train,epochs=10,batch_size=32,verbose=True,validation_data=(x_test,y_test))
        if stats: self.print_stats(history)

        # Saving model
        self.model.save("model.keras")
        return self.model


    def __init__(self,path=None,stats=False) -> None:
        if path: self.model = keras.models.load_model(path)
        else: self.model = self.train(stats=stats)
           

if __name__ == "__main__":
    model = Model("model.keras")
