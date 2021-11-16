import math

def getFloat(inputText):
    while True:
        try:
            return float(input(inputText));
        except:
            print("Invalid Input. Expected input: Float")

def getf(x, y):
    return math.exp(x) * math.sin(x)

def gety(x):
    return math.exp(x) * (math.sin(x) - math.cos(x)) / 2

def EulerMethod(h, x, w):
    return w + h * getf(x+h, w)

def RK(h, x, w):
    k1 = getf(x, w)
    k2 = getf(x + h/2, w + k1/2)
    k3 = getf(x + h/2, w + k2/2)
    k4 = getf(x + h, w + k3)
    return w + h * (k1 + 2 * (k2 + k3) + k4) / 6

h = getFloat("Enter the value for h: ")
x0 = getFloat("Enter the value for x0: ")
xn = getFloat("Enter the value for xn: ")
y0 = getFloat("Enter the value for y0: ")
n, EulerW, RKW = int((xn-x0)/h), y0, y0

for i in range(0, n):
    x = x0 + i * h
    EulerW = EulerMethod(h, x, EulerW)
    RKW = RK(h, x, RKW)

actualAnswer = gety(1)
print("\nAt x = 1")
print("Actual value of y \t\t\t\t=", actualAnswer)
print("\nEuler Method value of y \t\t=", EulerW)
print("Euler Method Error \t\t\t\t=", abs(100*(EulerW - actualAnswer)/actualAnswer))
print("\nRunge Kutta Method value of y \t=", RKW)
print("Runge Kutta Method Error \t\t=", abs(100*(RKW - actualAnswer)/actualAnswer))
