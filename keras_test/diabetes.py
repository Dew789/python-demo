# Create first network with Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy

def detect():
    # fix random seed for reproducibility
    seed = 8
    numpy.random.seed(seed)

    # load pima indians dataset
    dataset = numpy.loadtxt("/home/zh/pima-indians-diabetes.csv", delimiter=",")

    # split into input (X) and output (Y) variables
    X = dataset[:,0:8]
    Y = dataset[:,8]
    
    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=8, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(8, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))
    
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) # Fit the model
    model.fit(X, Y, epochs=150, batch_size=10)
    # evaluate the model
    scores = model.evaluate(X, Y)
    print("result %s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

if __name__ == '__main__':
    detect()
