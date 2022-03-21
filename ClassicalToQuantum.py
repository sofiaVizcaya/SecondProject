from MatrixMul import matrixMultiply
from Matrix import complexMatrixMultiply
import matplotlib.pyplot as plt
import numpy
def complexMatrixProbability(Matrix, Vector, Clicks = 1):
    for i in range (0, Clicks):
        if i == 0:
            Total = complexMatrixMultiply(Matrix, Vector)
        else:
            Total = complexMatrixMultiply(Matrix, Total)
    return Total
def amountofMarbles(Matrix, Vector, Clicks = 1):
    #function that tells us how many marbles we have after an amount of clicks.
    for i in range (0, Clicks):
        if i == 0:
            Total = matrixMultiply(Matrix, Vector)
        else:
            Total = matrixMultiply(Matrix, Total)
    return Total

def probabilityAfterClicks(Matrix, Vector, Clicks = 1):
    for i in range (0, Clicks):
        if i == 0:
            Total = matrixMultiply(Matrix, Vector)
        else:
            Total = matrixMultiply(Matrix, Total)
    return Total

def graphProbability(A):

    Dime = len(A)
    a = numpy.array([x for x in range(Dime)])
    b = numpy.array([round(A[a]*100, 3) for a in range(Dime)])
    plt.bar(a, b, color="green", align="center")
    plt.title('GraphProbability')
    plt.savefig("GraphProbability.png")
    plt.show()

Matrix = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1] ,[0, 0, 0, 1, 0, 0] ,[0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0]]
Vector = [[6], [2], [1], [5], [3], [10]]
print(amountofMarbles(Matrix, Vector, 1))
