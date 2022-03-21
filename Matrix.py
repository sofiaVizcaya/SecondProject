from Complex1 import complex_mult
from Complex1 import complex_sum
from Complex1 import conjugate
from Complex1 import complex_phase
def complex_sum (A, B):
    real = A[0] + B[0]
    Complex = A[1] + B[1]
    return real, Complex
def complex_mult(A, B):
    real = (A[0] * B[0]) + (A[1] * B[1] * -1.0)
    Complex = (A[0]*B[1]) + (A[1]*B[0])
    return real, Complex
def add_vector(A,B):
    C = []
    for i in range(0, len(A)):
        C[i] = complex_sum(A[i], B[i])
    return C
def addInverse (A):
    B = []
    B[0], B[1] = -1*A[0], -1*B[1]
    return B
def VectTimesScalar (A,c):
    B = []
    for i in range (0, len(A)):
        B[i] = A[0] * c, A[1] * c
    return B
def verifyComplexMatrixSum(A, B):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        return True
    else :
        return False
def complexMatrixSum(A, B):
    C = []
    if verifyComplexMatrixSum(A, B):
        for i in range (0, len(A)):
            for j in range (0, len(A[0])):
                C[i][j] = complex_sum(A[i][j] ,B[i][j])
    return C
def addInverseMat(A):
    C = []
    for i in range(0, len(A)):
        for j in range (0, len(A[0])):
            C[i][j] = (A[i][j][0] * -1), (A[i][j][1] * 1)
    return C
def multiplyScalarMatrix(A, c):
    B = []
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            B[i][j] = A[i][j][0] ** c, A[i][j][1] ** c
    return B
def transposed_matrix(A):
    B = []
    for i in range(0, len(A)):
        for j in range (0, len(A[0])):
            B[i][j] = A[j][i]
    return B
def transposed_vector(A):
    B = []
    for i in range(0, len(A)):
        B[i] = A[i]
def conjugate_matrix(A):
    B = []
    for i in range (0, len(A)):
        for j in range(0, len(A[0])):
            B[i][j] = conjugate(A[i][j])
    return B
def conjugate_vector(A):
    B = []
    for i in range(0, len(A)):
        B[i] = conjugate(A[i])
def verfProductMatrix(A, B):
    if len(A[0]) == len(B):
        return True
    else:
        return False

def complexMatrixComplement(A, B, i, j):
    Answer = [0, 0]
    for k in range (0, len(B)):
        X = complex_mult(A[i][k], B[k][j])
        Answer = complex_sum(Answer, X)
    return Answer
def complexMatrixMultiply(A, B):
    C = []
    for i in range (0, len(A)):
        C.append([])
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            C[i].append(complexMatrixComplement(A, B, i, j))
    return (C)
def complexInternalProduct(u, v):
    u, v = list(u), list(v)
    Answer = [0, 0]
    print(len(u))
    for i in range(0, len(u)):
        X = complex_mult(u[i], v[i])
        Answer = complex_sum(Answer, X)
    return Answer
def complexMatrixProbability(Matrix, Vector, Clicks = 1):
    for i in range (0, Clicks):
        if i == 0:
            Total = complexMatrixMultiply(Matrix, Vector)
        else:
            Total = complexMatrixMultiply(Matrix, Total)
    return Total

A = [[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],[0.0, 0.0], [0.0, 0.0]],
     [[0.7071, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],[0.0, 0.0], [0.0, 0.0]],
     [[0.7071, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],[0.0, 0.0], [0.0, 0.0]],
     [[0.0, 0.0], [-0.4082, 0.4082], [0.0, 0.0], [1.0, 0.0], [0.0, 0.0], [0.0, 0.0],[0.0, 0.0], [0.0, 0.0]],
     [[0.0, 0.0], [-0.4082, -0.4082], [0.0, 0.0], [0.0, 0.0], [1.0, 0.0], [0.0, 0.0],[0.0, 0.0], [0.0, 0.0]],
     [[0.0, 0.0], [0.4082, -0.4082], [-0.4082, 0.4082], [0.0, 0.0], [0.0, 0.0], [1.0, 0.0],[0.0, 0.0], [0.0, 0.0]],
     [[0.0, 0.0], [0.0, 0.0], [-0.4082, -0.4082], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],[1.0, 0.0], [0.0, 0.0]],
     [[0.0, 0.0], [0.0, 0.0], [0.4082, -0.4082], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],[0.0, 0.0], [1.0, 0.0]]]
B = [[[1.0 ,0]],
     [[0, 0]],
     [[0, 0]],
     [[0, 0]],
     [[0, 0]],
     [[0, 0]],
     [[0, 0]],
     [[0, 0]]]
print(complexMatrixProbability(A, B, 2))
C = [1, 2]
D = [[1, 2]]


