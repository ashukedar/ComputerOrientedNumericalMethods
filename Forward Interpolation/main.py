import math

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

def getFactorial(n):
    if(n == 1):
        return 1;
    else:
        return n * getFactorial(n-1);

def getDelTerm(i, deg):
    if deg == 1:
        return y[i+1] - y[i]
    return getDelTerm(i+1, deg-1) - getDelTerm(i, deg-1)

def getfx(val):
    fx = y[0]
    for i in range(1,n):
        mulTerm = 1
        for j in range(i):
            mulTerm *= val-x[j]
        fx += getDelTerm(0, i) * mulTerm / (getFactorial(i) * math.pow(h, i))
    return fx

x = []
y = []
n = getIntGreaterThan1("Enter the no. of points: ")
h = getFloat("Enter the value of h: ")
x.append(getFloat("Enter the value of x0: "))
y.append(getFloat("Enter the value of f(" + str(x[0]) + "): "))
for i in range(n-1):
    xi = x[i]+h
    x.append(xi)
    y.append(getFloat("Enter the value of f(" + str(xi) + "): "))
value = getFloat("Enter the value of x, whose corresponding f(x) is required: ")
print("f(" + str(value) + ") = " + str(getfx(value)))