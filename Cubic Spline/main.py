import bisect
import math
import numpy as np

def getIntGreaterThan1(inputText):
    while True:
        try:
            n = int(input(inputText));
            if(n >= 1):
                return n
            else:
                raise Exception()
        except:
            print("Invalid Input. Expected input: Integer greater than 0")

def getFloat(inputText):
    while True:
        try:
            return float(input(inputText));
        except:
            print("Invalid Input. Expected input: Float")

def getFdd():
    bigMatrix = arr = [[0 for i in range(n)] for j in range(n)]
    bigMatrix[0][0] = 1
    bigMatrix[n-1][n-1] = 1
    vector = [0,0]
    for i in range(1, n-1):
        bigMatrix[i][i-1] = x[i-1] - x[i]
        bigMatrix[i][i] = 2 * (x[i-1] - x[i+1])
        bigMatrix[i][i+1] = x[i] - x[i+1]
        vector.insert(i, 6 * (((y[i]-y[i-1])/(x[i]-x[i-1])) + ((y[i]-y[i+1])/(x[i+1]-x[i]))))
    arr = np.linalg.solve(np.array(bigMatrix), np.array(vector))
    print(bigMatrix, vector, arr)
    return arr

def getPx(val):
    i = bisect.bisect_left(x, val)
    print(i)
    diff = x[i] - x[i-1]
    result = math.pow(val - x[i], 3) * fdd[i-1] / (-6 * (diff))
    result += math.pow(val - x[i-1], 3) * fdd[i] / (6 * (diff))
    result += (val - x[i-1]) * y[i]/diff
    result -= (val - x[i-1]) * diff * fdd[i] / 6
    result -= (val - x[i]) * y[i-1] / diff
    result += (val - x[i]) * diff * fdd[i-1] / 6
    return result

n = 5
x = []
y = []
fdd = []
n = getIntGreaterThan1("Enter the no. of points: ")
for i in range(n):
    xi = getFloat("Enter the value of x(" + str(i) + "): ")
    x.append(xi)
    y.append(getFloat("Enter the value of f(" + str(xi) + "): "))
value = getFloat("Enter the value of x, whose corresponding f(x) is required: ")
fdd = getFdd().tolist();
print("f(" + str(value) + ") = " + str(getPx(value)))