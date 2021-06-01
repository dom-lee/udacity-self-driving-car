import numpy as np


# sigmoid function
def sigmoid(x):
    return 1/(1+np.exp(-x))


# Derivative of the sigmoid function
def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))


def main():
    learnrate = 0.5
    x = np.array([1, 2])
    y = np.array(0.5)

    # Initial weights
    w = np.array([0.5, -0.5])

    # Calculate one gradient descent step for each weight
    # TODO: Calculate output of neural network
    nn_output = sigmoid(np.dot(x, w))

    # TODO: Calculate output error of neural network
    error = y - nn_output

    # TODO: Calculate error term of neural network
    error_term = error * sigmoid_prime(np.dot(x, w))

    # TODO: Calculate change in weights
    del_w = learnrate * error * nn_output * (1 - nn_output) * x

    print('Neural Network output:')
    print(nn_output)
    print('Amount of Error:')
    print(error)
    print('Change in Weights:')
    print(del_w)


if __name__ == "__main__":
    main()
