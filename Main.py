import numpy as np



def fillMatrix():

    n = int(input("Gib den Grad der Gleichung an: "))
    n = n+1
    array = np.zeros((n, n+1))

    for i in range(0, n):
        for j in range(0, n+1):
            x = float(input("Gib die Stelle " + str(i) + " " + str(j) + " der Matrix ein: "))
            array[i][j] = x

    return array, n


def splitMatrix(x, y, matrix, n):

    if x != -1:
        y = 0
        result = []
        for y in range(0, n):
            k = 0
            l = 0
            if matrix[x][y] != 0:
                helpMatrix = np.zeros((n-1, n-1))
                for i in range(0, n):
                    for j in range(0, n):
                        if i != x and j != y:
                            helpMatrix[k][l] = matrix[i][j]
                            l += 1
                    if i != x:
                        l = 0
                        k += 1
                m = 1
                if (x + y) % 2 == 1:
                    m = -1
                helpMatrix[0][:] *= (matrix[x][y] * m)
                result.append(helpMatrix.copy())
    elif y != -1:
        x = 0
        result = []
        for x in range(0, n):
            k = 0
            l = 0
            if matrix[x][y] != 0:
                helpMatrix = np.zeros((n-1, n-1))
                for j in range(0, n):
                    for i in range(0, n):
                        if j != y and i != x:
                            helpMatrix[k][l] = matrix[i][j]
                            k += 1
                    if j != y:
                        k = 0
                        l += 1
                m = 1
                if (x + y) % 2 == 1:
                    m = -1
                helpMatrix[0][:] *= (matrix[x][y] * m)
                result.append(helpMatrix.copy())
    else:
        print("Error has occured in splitMatrix x == -1 and y == -1")

    return result, n-1                                                          #Matrix array



def searchZeros(n, matrix):

    maxZero = n
    i1 = -1
    j1 = -1
    for i in range(0, n):
        x = np.count_nonzero(matrix[i])
        if x < maxZero:
            i1 = i
            maxZero = x

    for j in range(0, n):
        x = np.count_nonzero(matrix[:, j])
        if x <= maxZero:
            i1 = -1
            j1 = j
            maxZero = x

    result, n = splitMatrix(i1, j1, matrix, n)

    return result, n                                                                #Matrix array

def calculate(n, matrix):                                                      #result Matrix array

    result, n = searchZeros(n, matrix)

    if result[0].size == 4:
        r = 0
        for i in result:
            r += calculate2x2Matrix(i.copy())
        return r
    else:
        r = 0
        for i in result:
            r += calculate(n, i.copy())
        return r

def createInitialMatrixArray(n):
    ds = []
    d = array[:, :n].copy()
    ds.append(d.copy())

    for i in range(0, n):
        d1 = array[:, :n].copy()
        d1[:, i] = array[:, n].copy()
        ds.append(d1.copy())

    return ds.copy()                                                             #List of Matrixs


def calculate2x2Matrix(matrix):

    r = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    return r

if __name__ == "__main__":

    array, n = fillMatrix()
    matrixArray = createInitialMatrixArray(n)                                     #Array aus Matrizen
    print()
    print()
    print()
    resultList = []
    if matrixArray[0].size == 4:
        for i in matrixArray:
            resultList.append(calculate2x2Matrix(i))
    else:
        for i in matrixArray:
            resultList.append(calculate(n, i))

    counter = resultList.__len__()-2
    for i in range(1, resultList.__len__()):
        resultList[i] = resultList[i] / resultList[0]
        if counter != 0:
            print(resultList[i], "x^", counter, "+ ")
        else:
            print(resultList[i])
        counter -= 1;