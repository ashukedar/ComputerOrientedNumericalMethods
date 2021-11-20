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

def getpx(x):
    return -3

def getqx(x):
    return 2

def getrx(x):
    return 2*x+3

def RK(h, x, w, getf, u1):
    k1 = getf(x, w, u1)
    k2 = getf(x + h/2, w + k1/2, u1)
    k3 = getf(x + h/2, w + k2/2, u1)
    k4 = getf(x + h, w + k3, u1)
    return w + h * (k1 + 2 * (k2 + k3) + k4) / 6

def getfForu2Fory1(x,y,u1):
    return getpx(x) * y + getqx(x) * u1 + getrx(x)

def gety1(x, prevy1, prevu2y1):
    newy1 = prevy1 + h * prevu2y1
    newu2y1 = RK(h, x, prevu2y1, getfForu2Fory1, prevy1)
    return newy1, newu2y1

def getfForu2Fory2(x,y,u2):
    return getpx(x) * y + getqx(x) * u2

def gety2(x, prevy2, prevu2y2):
    newy2 = prevy2 + h * prevu2y2
    newu2y2 = RK(h, x, prevu2y2, getfForu2Fory2, prevy2)
    return newy2, newu2y2

def gety(x, y1, y1b, y2, y2b):
    return y1 + (((beta - y1b)*y2)/y2b)

a = getFloat("Enter the value of a: ")#0
b = getFloat("Enter the value of b: ")#1
alpha = getFloat("Enter the value of alpha: ")#2
beta = getFloat("Enter the value of beta: ")#1
n = getIntGreaterThan1("Enter the value of n: ")#5
h = (b-a)/n

y1, u2y1, y2, u2y2, x = [alpha], [0], [0], [1], [a]

for i in range(1,n+1):
    x.append(a+i*h)
    newy1, newu2y1 = gety1(x[-1], y1[-1], u2y1[-1])
    u2y1.append(newu2y1)
    y1.append(newy1)
    newy2, newu2y2 = gety2(x[-1], y2[-1], u2y2[-1])
    u2y1.append(newu2y2)
    y2.append(newy2)

for i in range(n+1):
    print("\nAt x =", x[i])
    calcy = gety(x[i], y1[i], y1[-1], y2[i], y2[-1])
    print('\ty =', calcy)