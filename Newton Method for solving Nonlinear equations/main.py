import numpy as np
import sympy as sym

def Jacobian(v_str, f_list):
    vars = sym.symbols(v_str)
    f = sym.sympify(f_list)
    J = sym.zeros(len(f),len(vars))
    for i, fi in enumerate(f):
        for j, s in enumerate(vars):
            J[i,j] = sym.diff(fi, s)
    return J

def getFloat(inputText):
    while True:
        try:
            return float(input(inputText));
        except:
            print("Invalid Input. Expected input: Float")

def getf1(x,y):
    return x + x*y - 4
    
def getf2(x,y):
    return x + y - 3

def getF(x,y):
    return [[getf1(x,y)],[getf2(x,y)]]

def done(F, errorTolerancef1, errorTolerancef2):
    return abs(F[0][0]) <= errorTolerancef1 and abs(F[1][0]) <= errorTolerancef2

def getJacobian(x,y):
    J = Jacobian('u1 u2', ['u1 + u1*u2 - 4','u1 + u2 - 3'])
    u1, u2 = x, y
    for i in range(2):
        for j in range(2):
            J[i+j] = eval(str(J[i+j]))
    return np.matrix([[J[0],J[1]],[J[2],J[3]]], dtype='float')

errorTolerancef1 = getFloat("Enter the error tolerance for f1: ")
errorTolerancef2 = getFloat("Enter the error tolerance for f2: ")
x = getFloat("Enter the initial guess for x: ")
y = getFloat("Enter the initial guess for y: ")
F = getF(x,y)

while not done(F, errorTolerancef1, errorTolerancef2):
#for i in range(5):
    J = getJacobian(x,y)
    arr = np.linalg.solve(np.array(J), np.array(F))
    x -= arr[0][0]
    y -= arr[1][0]
    F = getF(x,y)

print("\nFinal Solution(x,y): (", x, ",", y, ")")
print("For these value,\nthe value of f1 is", getf1(x,y))
print("And value of f2 is", getf2(x,y))