import math
import scipy.integrate as integrate

def getFloat(inputText):
    while True:
        try:
            return float(input(inputText));
        except:
            print("Invalid Input. Expected input: Float")

def getfx(x):
    return 3 - 11 * math.pow((1-math.pow(x,2)), 2.5)

def getfix(x, a, b):
    return getfx(((b-a)*x + b+a)/2)

def getExactIntegration(a, b):
    return integrate.quad(getfx, a, b)

def integrate2(a, b):
    root3 = math.pow(3,1/2)
    t1, t2 = 1/root3, -1/root3
    w1, w2 = 1, 1
    return ((b-a)/2) * (w1 * getfix(t1, a, b) + w2 * getfix(t2, a, b))

def integrate3(a,b):
    rootpoint6 = math.pow(0.6,1/2)
    w1, w2, w3 = 5/9, 8/9, 5/9
    t1, t2, t3 = rootpoint6, 0, -1*rootpoint6
    return ((b-a)/2) * (w1 * getfix(t1, a, b) + w2 * getfix(t2, a, b) + w3 * getfix(t3, a, b))

#def integrate4(a,b):
    #t1, t2 = math.pow((3-2*math.pow(6/5,1/2))/7,1/2), -1 * math.pow((3-2*math.pow(6/5,1/2))/7,1/2)
    #t3, t4 = math.pow((3+2*math.pow(6/5,1/2))/7,1/2), -1 * math.pow((3+2*math.pow(6/5,1/2))/7,1/2)
    #w1, w2 = (18+math.pow(30,1/2))/36, (18+math.pow(30,1/2))/36
    #w3, w4 = (18-math.pow(30,1/2))/36, (18-math.pow(30,1/2))/36
    #return ((b-a)/2) * (w1*getfix(t1, a, b) + w2*getfix(t2, a, b) + w3*getfix(t3, a, b) + w4*getfix(t4, a, b))

a = getFloat("Enter the value of lower limit of integral: ")
b = getFloat("Enter the value of upper limit of integral: ")
exact = getExactIntegration(a, b)[0]
print("Exact Integral:", exact, "\n")

print("With 2 points:")
integral = integrate2(a,b)
print("Integration:", integral)
print("Error: ", str(abs(100 * (exact - integral)/exact)), "\n")

print("With 3 points: ")
integral = integrate3(a,b)
print("Integration:", integral)
print("Error: ", str(abs(100 * (exact - integral)/exact)), "\n")

#print("With 4 points: ")
#integral = integrate4(a,b)
#print("Integration:", integral)
#print("Error: ", str(abs(100 * (exact - integral)/exact)))