# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 10:50:20 2025

@author: mkamr
"""

import numpy as np

def printMatrix(A, start, rows, cols):
    for i in range(start[0], start[0] + rows):
        for j in range(start[1], start[1] + cols):
            print(A[i][j], end=' ')
        print()

def MatAdd(A, B):
    r, c = len(A), len(A[0])
    R = [[A[i][j] + B[i][j] for j in range(c)] for i in range(r)]
    return R

def MatAddPartial(A, B, start, size):
    x, y = start
    R = [[A[i][j] + B[i][j] for j in range(y, y + size)] for i in range(x, x + size)]
    return R

def MatMul(A, B):
    r1, c1 = len(A), len(A[0])
    r2, c2 = len(B), len(B[0])
    R = [[0 for _ in range(c2)] for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                R[i][j] += A[i][k] * B[k][j]
    return R

def MatMulRecursive(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    k = n // 2
    A11 = [[A[i][j] for j in range(k)] for i in range(k)]
    A12 = [[A[i][j] for j in range(k, n)] for i in range(k)]
    A21 = [[A[i][j] for j in range(k)] for i in range(k, n)]
    A22 = [[A[i][j] for j in range(k, n)] for i in range(k, n)]
    B11 = [[B[i][j] for j in range(k)] for i in range(k)]
    B12 = [[B[i][j] for j in range(k, n)] for i in range(k)]
    B21 = [[B[i][j] for j in range(k)] for i in range(k, n)]
    B22 = [[B[i][j] for j in range(k, n)] for i in range(k, n)]
    C11 = MatAdd(MatMulRecursive(A11, B11), MatMulRecursive(A12, B21))
    C12 = MatAdd(MatMulRecursive(A11, B12), MatMulRecursive(A12, B22))
    C21 = MatAdd(MatMulRecursive(A21, B11), MatMulRecursive(A22, B21))
    C22 = MatAdd(MatMulRecursive(A21, B12), MatMulRecursive(A22, B22))
    R = [[0]*n for _ in range(n)]
    for i in range(k):
        for j in range(k):
            R[i][j] = C11[i][j]
            R[i][j+k] = C12[i][j]
            R[i+k][j] = C21[i][j]
            R[i+k][j+k] = C22[i][j]
    return R

def MatMulStrassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0]*B[0][0]]]
    k = n//2
    A11 = [[A[i][j] for j in range(k)] for i in range(k)]
    A12 = [[A[i][j] for j in range(k,n)] for i in range(k)]
    A21 = [[A[i][j] for j in range(k)] for i in range(k,n)]
    A22 = [[A[i][j] for j in range(k,n)] for i in range(k,n)]
    B11 = [[B[i][j] for j in range(k)] for i in range(k)]
    B12 = [[B[i][j] for j in range(k,n)] for i in range(k)]
    B21 = [[B[i][j] for j in range(k)] for i in range(k,n)]
    B22 = [[B[i][j] for j in range(k,n)] for i in range(k,n)]
    M1 = MatMulStrassen(MatAdd(A11, A22), MatAdd(B11, B22))
    M2 = MatMulStrassen(MatAdd(A21, A22), B11)
    M3 = MatMulStrassen(A11, [[B12[i][j]-B22[i][j] for j in range(k)] for i in range(k)])
    M4 = MatMulStrassen(A22, [[B21[i][j]-B11[i][j] for j in range(k)] for i in range(k)])
    M5 = MatMulStrassen(MatAdd(A11, A12), B22)
    M6 = MatMulStrassen([[A21[i][j]-A11[i][j] for j in range(k)] for i in range(k)], MatAdd(B11, B12))
    M7 = MatMulStrassen([[A12[i][j]-A22[i][j] for j in range(k)] for i in range(k)], MatAdd(B21, B22))
    C11 = MatAdd(MatAdd(M1, M4), [[-M5[i][j] + M7[i][j] for j in range(k)] for i in range(k)])
    C12 = MatAdd(M3, M5)
    C21 = MatAdd(M2, M4)
    C22 = MatAdd(MatAdd(M1, M3), [[-M2[i][j] + M6[i][j] for j in range(k)] for i in range(k)])
    R = [[0]*n for _ in range(n)]
    for i in range(k):
        for j in range(k):
            R[i][j] = C11[i][j]
            R[i][j+k] = C12[i][j]
            R[i+k][j] = C21[i][j]
            R[i+k][j+k] = C22[i][j]
    return R
