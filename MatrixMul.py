import math
#mult matrices
def matrixComplement(A, B, i, j):
    Answer = 0
    for k in range (0, len(B)):
        Answer = Answer + (A[i][k] * B[k][j])
    return Answer
def matrixMultiply(A, B):
    C = []
    for i in range (0, len(A)):
        C.append([])
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            C[i].append(matrixComplement(A, B, i, j))
    return(C)
def complexMatrixComplement(A, B, i, j):
    Answer = [0, 0]
    for k in range (0, len(B)):
        X = complex_mul(A[i][k], B[k][j])
        Answer = complex_sum(Answer, X)
    return Answer
    
def AmountofMarbles(Matrix, Vector, Clicks=0):
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

M = [[0, 1/6, 5/6], [1/3, 1/2, 1/6], [2/3, 1/3, 0]]
V = [[1/6], [1/6], [2/3]]
print(probabilityAfterClicks(M, V, 3))

