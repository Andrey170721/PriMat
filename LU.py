import numpy as np
from scipy import sparse

k = 0

def decompose_to_LU(a):
    lu_matrix = np.matrix(np.zeros([a.shape[0], a.shape[1]]))
    n = a.shape[0]

    for k in range(n):
        for j in range(k, n):
            lu_matrix[k, j] = a[k, j] - lu_matrix[k, :k] * lu_matrix[:k, j]
        for i in range(k + 1, n):
            lu_matrix[i, k] = (a[i, k] - lu_matrix[i, : k] * lu_matrix[: k, k]) / lu_matrix[k, k]

    return lu_matrix


def get_L(m):
    L = m.copy()
    for i in range(L.shape[0]):
            L[i, i] = 1
            L[i, i+1 :] = 0
    return np.matrix(L)


def get_U(m):
    U = m.copy()
    for i in range(1, U.shape[0]):
        U[i, :i] = 0
    return U

def solve_LU(lu_matrix, b):
    y = np.matrix(np.zeros([lu_matrix.shape[0], 1]))
    for i in range(y.shape[0]):
        y[i, 0] = b[i, 0] - lu_matrix[i, :i] * y[:i]

    x = np.matrix(np.zeros([lu_matrix.shape[0], 1]))
    for i in range(1, x.shape[0] + 1):
        x[-i, 0] = (y[-i] - lu_matrix[-i, -i:] * x[-i:, 0] )/ lu_matrix[-i, -i]

    return x


if __name__ == '__main__':
    l = sparse.lil_matrix((5, 5))
    xx = np.matrix(([1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]))
    l[0, 0] = 1.0
    l[0, 1] = 1.5
    l[0, 3] = 3.0
    l[1, 0] = 2.0
    l[1, 1] = 5.0
    l[2, 2] = 4.0
    l[2, 3] = 6.0
    l[2, 4] = 7.0
    l[3, 0] = 4.0
    l[3, 2] = 2.0
    l[3, 3] = 7.0
    l[4, 1] = 8.5
    l[4, 4] = 5.0
    #for i in range(l.shape[0]):
        #for j in range(l.shape[1]):
            #if i == j:
                #l[i, j] = 0
                #for s in range(l.shape[1]):
                    #l[i, j] += l[i, s] + 10 ** -k
    #f = l * xx
    #print(l.toarray())
    #print(f)
    #LU = decompose_to_LU(l)
    #print(LU)

    #print(solve_LU(LU, f).transpose())

    c = np.zeros((20, 20))

    for i in range(c.shape[0]):
        for j in range(c.shape[1]):
           c[i][j] = 1 / ((i + 1) + (j + 1) - 1)
    d = c * xx

    print(c)
    print(xx)
    LU = decompose_to_LU(c)
    print(solve_LU(LU, d).transpose())
