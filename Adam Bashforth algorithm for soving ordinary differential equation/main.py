def getf(x,y):
    return (2-2*x*y)/(1+x**2)

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

def getExacty(x):
    return (2*x + 1)/(x**2 + 1)

def getFloat(inputText):
    while True:
        try:
            return float(input(inputText));
        except:
            print("Invalid Input. Expected input: Float")

def RK(h, x, w):
    k1 = getf(x, w)
    k2 = getf(x + h/2, w + k1/2)
    k3 = getf(x + h/2, w + k2/2)
    k4 = getf(x + h, w + k3)
    return w + h * (k1 + 2 * (k2 + k3) + k4) / 6

def AdamBashforth(h, x, w):
    return w[2] + h * (23 * getf(x[2], w[2]) - 16 * getf(x[1], w[1]) + 5 * getf(x[0], w[0])) / 12

x0 = getFloat("Enter the value of lower limit(a): ")
xn = getFloat("Enter the value of upper limit(b): ")
h = getFloat("Enter the value of difference(h): ")
y0 = getFloat("Enter the value of y[0]: ")
n, w, x = int((xn-x0)/h), [y0], [x0]

for i in range(1, 3):
    x.append(x0 + i * h)
    w.append(RK(h, x[-2], w[-1]))

for i in range(3, n+1):
    w.append(AdamBashforth(h, x[-3:], w[-3:]))
    x.append(x0 + i * h)

for i in range(len(x)):
    exact = getExacty(x[i])
    calc = w[i]
    print('\nAt x = ', x[i])
    print('Exact: ', exact)
    print('Calc: ', calc)
    print('Error Percentage: ', 100 * abs(exact-calc)/exact)