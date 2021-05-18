import numpy as np

def randomization(n):
    """
    Arg:
      n - an integer
    Returns:
      A - a randomly-generated nx1 Numpy array.
    """
    if n > 0:
        return np.random.random([n, 1])
    return []

 print(randomization(1))

def operations(h, w):
    """
    Takes two inputs, h and w, and makes two Numpy arrays A and B of size
    h x w, and returns A, B, and s, the sum of A and B.

    Arg:
      h - an integer describing the height of A and B
      w - an integer describing the width of A and B
    Returns (in this order):
      A - a randomly-generated h x w Numpy array.
      B - a randomly-generated h x w Numpy array.
      s - the sum of A and B.
    """
    np_array_a = np.random.random((h, w))
    np_array_b = np.random.random((h, w))
    
    return [np_array_a, np_array_b, np_array_a + np_array_b]

 print(operations(1,2))
    #raise NotImplementedError


def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, and returns the L2 norm of their
    sum.

    Arg:
      A - a Numpy array
      B - a Numpy array
    Returns:
      s - the L2 norm of A+B.
    """
    return np.linalg.norm(A+B)
    #raise NotImplementedError
    
array_n1 = operations(3,4)
array_n2 = operations(2,5)
print(norm(array_n1[0],array_n1[1]))
print(norm())

def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    product = inputs*weights
    return np.array([[np.tanh(np.sum(product))]])


    print(neural_network(np.array([1, 2]), np.array([2, 3])))
    #raise NotImplementedError
    
    print(scalar_function(3,10))

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    if(x > y):
        return x/y
    else:
        return x*y
    #raise NotImplementedError

def vector_function(x, y):
    """
    Make sure vector_function can deal with vector input x,y 
    """
    v_fn = np.vectorize(scalar_function)
    return v_fn(x, y)
    #raise NotImplementedError
    
    print(vector_function([10,2],[3,4]))

