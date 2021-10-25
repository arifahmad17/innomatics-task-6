import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    b=arr[::-1]
    b=numpy.array(b,float)
    return b
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
