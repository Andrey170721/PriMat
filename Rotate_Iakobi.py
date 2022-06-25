import numpy as np

def Jacobi(matrix, n, eigenvectors, eigenvalues, precision, max):

    for i in range(0, n - 1):
        eigenvectors[i * n + i] = 1.0
        for j in range(0, n - 1):
            if i != j:
                eigenvectors[i * n + j] = 0.0

    nCount = 0
    while 1:
        db_max = matrix[1]
        n_row = 0
        n_col = 1
        for i in range(0, n - 1):
            for j in range(0, n - 1):
                d = np.fabs(matrix[i * n + j])
                if i != j and d > db_max:
                    db_max = d
                    n_row = i
                    n_col = j

        if db_max < precision:
            break
        if nCount > max:
            break

        nCount+=nCount

        dbApp = matrix[n_row * n + n_row]
        dbApq = matrix[n_row * n + n_col]
        dbAqq = matrix[n_col * n + n_col]
        dbAngle = 0.5*np.arctan2(-2 * dbApq, dbAqq - dbApp)
        dbSinTheta = np.sin(dbAngle)
        dbCosTheta = np.cos(dbAngle)
        dbSin2Theta = np.sin(2 * dbAngle)
        dbCos2Theta = np.cos(2 * dbAngle)
        matrix[n_row * n + n_row] = dbApp * dbCosTheta * dbCosTheta + dbAqq * dbSinTheta * dbSinTheta + 2 * dbApq * dbCosTheta * dbSinTheta
        matrix[n_col * n + n_col] = dbApp * dbSinTheta * dbSinTheta + dbAqq * dbCosTheta * dbCosTheta - 2 * dbApq * dbCosTheta * dbSinTheta
        matrix[n_row * n + n_col] = 0.5 * (dbAqq - dbApp) * dbSin2Theta + dbApq * dbCos2Theta
        matrix[n_col * n + n_row] = matrix[n_row * n + n_col]

        for i in range(0, n - 1):
                if i != n_col and i != n_row:
                    u = i * n + n_row
                    w = i * n + n_col
                    db_max = matrix[u]
                    matrix[u] = matrix[w] * dbSinTheta + db_max * dbCosTheta
                    matrix[w] = matrix[w] * dbCosTheta - db_max * dbSinTheta

        for j in range(0, n - 1):
            if j != n_col and j != n_row:
                u = n_row * n + j
                w = n_col * n + j
                db_max = matrix[u]
                matrix[u] = matrix[w] * dbSinTheta + db_max * dbCosTheta
                matrix[w] = matrix[w] * dbCosTheta - db_max * dbSinTheta

        for i in range(0, n):
            u = i * n + n_row
            w = i * n + n_col
            db_max = eigenvectors[u]
            eigenvectors[u] = eigenvectors[w] * dbSinTheta + db_max * dbCosTheta
            eigenvectors[w] = eigenvectors[w] * dbCosTheta - db_max * dbSinTheta

    mapEigen = list()
    for i in range(0, n):
        eigenvalues[i] = matrix[i * n + i]
        v = [eigenvalues[i], i]
        mapEigen.append(v)

    pdbTmpVec = [n * n]
    iter = mapEigen
    for j in range(0, n - 1):
        for i in range(0, n):
            pdbTmpVec[i * n + j] = eigenvectors[i * n + iter[j][2]]

        eigenvalues[j] = iter[j][1]

    for i in range(0, n):
        dSumVec = 0
        for j in range(0, n):
            dSumVec += pdbTmpVec[j * n + i]
        if dSumVec < 0:
            for j in range(0, n):
                pdbTmpVec[j * n + i] *= -1

    return True



if __name__ == '__main__':

    a = np.matrix(( (1, 1.5, 0, 3, 0), (2, 5, 0, 0, 0),(0, 0, 4, 6, 7),(4, 0, 2, 7, 0), (0, 8.5, 0, 0, 5)))
    n = 4
    eps = 1e-5
    T = 10000
    p = np.zeros((4, 4))
    v= np.zeros(4)
    re = Jacobi(a, n, p, v, eps, T)
    if re:
        print('Матрица: ')
        for i in range(0, n):
            for  j in range(0, n):
                print(a)

        print('Собственный вектор: ')
        for i in range(0, n):
            for j in range(0, n):
                print(p)

        print('Собственные значения: ')
        for i in range(0, n):
                print(v[i])
    else:
        print('false')
