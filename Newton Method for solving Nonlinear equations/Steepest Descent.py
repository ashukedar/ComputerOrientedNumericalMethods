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

def Hessian(v_str):
    vars = sym.symbols(v_str)
    g = '(' + getExp1() + ')** 2 + (' + getExp2() + ')**2'
    exp1 = sym.diff(sym.diff(g,vars[0]),vars[0])
    exp2 = sym.diff(sym.diff(g,vars[0]),vars[1])
    exp3 = sym.diff(sym.diff(g,vars[1]),vars[0])
    exp4 = sym.diff(sym.diff(g,vars[1]),vars[1])
    return [[exp1,exp2],[exp3,exp4]]

def getFloat(inputText):
    while True:
        try:
            return float(input(inputText));
        except:
            print("Invalid Input. Expected input: Float")

def getSymbols():
    return 'u1 u2'

def getExp1():
    return 'u1 * u2 - 1'

def getExp2():
    return 'u1**2 * u2**2 - 1'

def getf1(u1,u2):
    return eval(getExp1())

def getf2(u1,u2):
    return eval(getExp2())

def getF(x,y):
    return [[getf1(x,y)],[getf2(x,y)]]

def getg(x,y):
    return getf1(x, y)**2 + getf2(x, y)**2

def done(F, errorTolerancef1, errorTolerancef2):
    return abs(F[0][0]) <= errorTolerancef1 and abs(F[1][0]) <= errorTolerancef2

def getJacobian(x,y):
    J = Jacobian(getSymbols(), [getExp1(),getExp2()])
    print('Jacobian:', J)
    u1, u2 = x, y
    for i in range(4):
        J[i] = eval(str(J[i]))
    return np.matrix([[J[0],J[1]],[J[2],J[3]]], dtype='float')

def getHessian(x,y):
    H = Hessian(getSymbols())
    print('Hessian:', H)
    u1, u2 = x, y
    for i in range(2):
        for j in range(2):
            H[i][j] = eval(str(H[i][j]))
    return np.matrix(H, dtype='float')

def getdelg(x,y,F):
    J = getJacobian(x, y)
    print('Jacobian for x:', J)
    print('Jacobian Transpose:', np.matrix(J).transpose())
    mat = np.dot(np.matrix(J).transpose(), F)
    print('Jacobian Transpose * F:', mat)
    return 2 * mat

def getalpha(x,y,F):
    delg = getdelg(x,y,F)
    print('delg: 2 * Jacobian Transpose * F:', delg)
    delgT = np.matrix(delg).transpose()
    print('delg Transpose:', delgT)
    numerator = np.dot(delgT,delg)[0]
    h = getHessian(x, y)
    print('Hessian for x:', h)
    print('delg Transpose * Hessian:', np.dot(delgT, h))
    denominator = np.dot(np.dot(delgT, h), delg)
    print('numerator: delgTranspose * delg:', numerator)
    print('denominator: delg Transpose * Hessian * delg:', denominator)
    return [numerator/denominator, delg]

errorTolerancef1 = getFloat("Enter the error tolerance for f1: ")
errorTolerancef2 = getFloat("Enter the error tolerance for f2: ")
x = getFloat("Enter the initial guess for x: ")
y = getFloat("Enter the initial guess for y: ")
F = getF(x,y)
print('F: ', F)
i = 1

while not done(F, errorTolerancef1, errorTolerancef2):
#for i in range(5):
    print('\n\nIteration:', i)
    arr = getalpha(x, y, F)
    alpha, delg = arr[0].tolist()[0][0], arr[1]
    print('alpha: numerator/denominator:', alpha)
    print('alpha * delg[0]', alpha * delg[0].tolist()[0][0])
    x -= alpha * delg[0].tolist()[0][0]
    print('new X: x - alpha * delg[0]:', x)
    print('alpha * delg[1]', alpha * delg[1].tolist()[0][0])
    y -= alpha * delg[1].tolist()[0][0]
    print('new Y: y - alpha * delg[1]:', y)
    F = getF(x,y)
    print('new F:', F)
    i+=1

print("\nFinal Solution(x,y): (", x, ",", y, ")")
print("For these value,\nthe value of f1 is", getf1(x,y))
print("And value of f2 is", getf2(x,y))