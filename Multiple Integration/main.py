import math
from scipy import integrate

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

def getfxy(x, y):
    return math.pow(x,3) + math.pow(y,2) + x * y

def getfyx(y, x):
    return math.pow(x,3) + math.pow(y,2) + x * y

def getExactResult():
    return integrate.dblquad(getfyx, a, b, lambda x: c, getd)

def getd(x):
    return x + 5.08182

def getResult():
    h = (b-a)/n
    x = []
    d = []
    k = []
    for i in range(n+1):
        x.append(a + i*h)
        d.append(getd(x[-1]))
        k.append((d[-1] - c)/m)
    result =  k[0] * getfxy(a, c) + k[-1] * getfxy(b, c)
    result += k[0] * getfxy(a, d[0]) + k[-1] * getfxy(b, d[-1])
    for i in range(1,n):
        result += 2 * k[i] * getfxy(x[i],c)
        result += 2 * k[i] * getfxy(x[i],d[i])
    for j in range(1,m):
        result += 2 * k[0] * getfxy(a,c+j*k[0])
        result += 2 * k[-1] * getfxy(b,c+j*k[-1])
    for i in range(1,n):
        x1 = x[i]
        k1 = k[i]
        for j in range(1,m):
            result += 4 * k1 * getfxy(x1,c+j*k1)
    return result * h / 4

a = getFloat("Enter the a: ")
b = getFloat("Enter the b: ")
c = getFloat("Enter the c: ")
print("\nd = x + 5.08182")
n = getIntGreaterThan1("Enter the n: ")
m = getIntGreaterThan1("Enter the m: ")

exact = getExactResult()
result = getResult()
print("\nExpected result:", exact[0])
print("Result:", result)
print("Error: ", abs(exact[0]-result)*100/exact[0])