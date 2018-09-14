import numpy as np
from sklearn.metrics import classification_report
from copy import copy
import matplotlib.pyplot as plt
import scipy


def sigmoid(scores):
    return scipy.special.expit(scores)


def logistic_regression(features, target, learning_rate, add_intercept=False):
    if add_intercept:
        intercept = np.ones((features.shape[0], 1))
        features = np.hstack((intercept, features))

    weights = np.zeros(features.shape[1])

    previous_weights = copy(weights)

    step = 0
    while True:
        step += 1
        scores = np.dot(features, weights)
        predictions = sigmoid(scores)

        # Update weights with gradient
        output_error_signal = target - predictions
        gradient = np.dot(features.T, output_error_signal)
        weights += learning_rate * gradient
        delta_weights = np.subtract(previous_weights, weights)

        if np.linalg.norm(delta_weights) <= 10:
            break
        else:
            previous_weights = copy(weights)

    return weights, step



def cross_validation(data, lr):

    total_acc = 0
    steps = 0
    total_preds = np.ndarray(shape=(0,))
    total_labels = np.ndarray(shape=(0,))
    for i in range(5):
        start = round(i * (len(data) / 5))
        end = round((i + 1) * (len(data)/5))
        test_set = data[start:end,:]
        train_set = np.vstack((data[0:start,:], data[end:, :]))


        v_features = np.vstack((train_set[:, :4])).astype(np.float32)
        v_labels = np.hstack((train_set[:, 4:5]))
        weights, step = logistic_regression(v_features, v_labels, learning_rate=lr, add_intercept=True)

        test_labels = test_set[:, 4]
        test_features = test_set[:, :4]

        final_scores = np.dot(np.hstack((np.ones((test_features.shape[0], 1)),
                                         test_features)), weights)
        preds = np.round(sigmoid(final_scores))

        total_preds = np.append(total_preds, preds)
        total_labels = np.append(total_labels, test_labels)

        acc = (preds == test_labels).sum().astype(float) / len(preds)
        steps += step

    total_acc += acc
    print("Learning rate {0} took {1} steps to converge.".format(lr, steps))
    print("Learning rate {1} resulted in total Accuracy {0:.5f}.".format(total_acc, lr))
    report = classification_report(total_labels, total_preds, digits=5)
    print("Learning rate {0} yielded these results:".format(lr) + "\n" + report)


    return steps, lr


data = np.loadtxt("data_banknote_authentication.txt", dtype=float, delimiter=",")

learning_rates = [0.1, 0.3, 0.5, 0.7, 0.9]

s = []
r = []
for i in range(len(learning_rates)):
    steps, lr = cross_validation(data, learning_rates[i])
    s.append(steps)
    r.append(lr)

#Draw the plot
plt.plot(r,s, "ro")

plt.show()