import numpy as np
def sigmoid(x):
    """
    Compute the sigmoid function for the input here.
    Arguments:
    x -- A scalar or numpy array.
    Return:
    s -- sigmoid(x)
    """

    ### YOUR CODE HERE
    s=np.divide(np.exp(x),1+np.exp(x))
    ### END YOUR CODE

    return s

a=np.array([1,2,3])
print(sigmoid(a))