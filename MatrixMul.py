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
    
