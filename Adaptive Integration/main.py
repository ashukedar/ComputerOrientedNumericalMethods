import math
import numpy as np
from matplotlib import pyplot as plt

#Function to get fx corresponding to given x
def getfx(x):
    return math.cos(x-4) - x * math.sin(x-4)

#Function to get exact values of integral for given x
def exact(x):
    return x * math.cos(x-4)

#Function to get integration between a and b with divisions number of steps 
#and prev value of integration at a
def getArea(a, b, divisions, prev):
    h = ((b-a)/divisions)
    x0 = a
    x1 = a + h
    area = prev
    x = [x0]
    y = [prev]
    integrate = 0
    while x1 <= b:
        temp = h * (getfx(x0) + getfx(x1)) / 2
        area += temp
        x1 += h
        x0 += h
        x.append(x0)
        y.append(area)
        integrate += temp
    return area, integrate, x, y

#Generic function to get float type user input
def getFloat(inputText):
    while True:
        try:
            return float(input(inputText));
        except:
            print("Invalid Input. Expected input: Float")

#setup
i = 1
steps = 1
stepSizeList = []
prev = 5.03443
ans = 0
x = []
y = []

#Get input fro user
a = getFloat("Enter the value of a: ")
b = getFloat("Enter the value of b: ")
errorTolerance = getFloat("Enter the value of error tolerance: ")

#Base case integration
area1, ans, x, y = getArea(a,b,steps,prev)
area2, ans, x, y = getArea(a,b,steps*2,prev)
i+=1
error = abs(area1 - area2)/(math.pow(2,i)-1)
stepSizeList.append((b-a)/steps)

#Calculate integration with lesser and lesser step size while error > errorTolerance
while error > errorTolerance:
    steps *= 2
    area1 = area2
    area2, ans, x, y = getArea(a,b,steps*2,prev)
    error = abs(area1 - area2)/3
    stepSizeList.append((b-a)/steps)
    i+=1

#Output
print("Integration between -6 to 6:", ans)
print("Error while calulating integration:", error)

#Plot graph for actual Values and predicted values
plt.figure(1)
plt.scatter(x,y,color='r',s=3.5)
points = np.linspace(a, b, 1000)
plt.plot(points, [exact(i) for i in points], c='b')
plt.legend(['Actual Values','Predicte Values'])

#Plot graph of step size vs iteration
plt.figure(2)
plt.xlabel("Iteration")
plt.ylabel("Step size")
plt.plot([(i+1) for i in range(len(stepSizeList))], stepSizeList)