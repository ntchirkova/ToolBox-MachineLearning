""" Exploring learning curves for classification of handwritten digits """

import matplotlib.pyplot as plt
import numpy
import statistics
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression


def display_digits():
    digits = load_digits()
    print(digits.DESCR)
    fig = plt.figure()
    for i in range(10):
        subplot = fig.add_subplot(5, 2, i+1)
        subplot.matshow(numpy.reshape(digits.data[i], (8, 8)), cmap='gray')

    plt.show()


def train_model():
    data = load_digits()
    num_trials = 10
    train_percentages = range(5, 95, 5)
    test_accuracies = []#numpy.zeros(len(train_percentages))

    # train models with training percentages between 5 and 90 (see
    # train_percentages) and evaluate the resultant accuracy for each.
    # You should repeat each training percentage num_trials times to smooth out
    # variability.
    # For consistency with the previous example use
    # model = LogisticRegression(C=10**-10) for your learner

    for i in train_percentages:

        tests = []
        for t in range(0,num_trials):
            X_train, X_test, y_train, y_test = train_test_split(data.data, data.target,
            train_size=i/100)
            model = LogisticRegression(C=10**-12)
            model.fit(X_train, y_train)
            score = model.score(X_test, y_test)
            tests.append(score)
        avg = statistics.mean(tests)

        test_accuracies.append(avg)


# data = load_digits()
# X_train, X_test, y_train, y_test = train_test_split(data.data, data.target,
# train_size=0.5)
# model = LogisticRegression(C=10**-10)
# model.fit(X_train, y_train)
# print("Train accuracy %f" %model.score(X_train, y_train))
# print("Test accuracy %f"%model.score(X_test, y_test))
    fig = plt.figure()
    plt.plot(train_percentages, test_accuracies)
    plt.xlabel('Percentage of Data Used for Training')
    plt.ylabel('Accuracy on Test Set')
    plt.show()




if __name__ == "__main__":
    # Feel free to comment/uncomment as needed
    train_model()
    # train_model()
