import numpy as np

def m(prompt):
    print(prompt)
    inputrow = int(input("행의 수 : "))
    inputcol = int(input("열의 수 : "))
    matrix = []
    for i in range(inputrow):
        matrix_row = list(map(float, input(f"행 {i + 1}의 성분 입력(공백구분) : ").split()))
        matrix.append(matrix_row)

    return np.array(matrix)

def eigenvalues_vectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

def svd(matrix):
    U, S, Vt = np.linalg.svd(matrix)
    return U, S, Vt                 

def matrix_rank(matrix):
    return np.linalg.matrix_rank(matrix)

def basis_transformation_matrix(alpha, beta):
    alpha_inv = np.linalg.inv(alpha)
    Q = np.dot(beta, alpha_inv)
    return Q

def matrix_trace(matrix):
    trace = np.trace(matrix)
    return trace
