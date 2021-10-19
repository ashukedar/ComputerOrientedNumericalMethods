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

def getUnknowns():
    y = [c[0]/b[0]]
    d = [u[0]/b[0]]
    for i in range(1,n):
        y.append(c[i]/(b[i]-a[i]*y[-1]))
        d.append((u[i]-a[i]*d[-1])/(b[i]-a[i]*y[-2]))
    unknowns = [d[-1]]
    for i in range(1,n):
        index = n-i-1
        unknowns.insert(0,d[index] - y[index] * unknowns[0])
    return unknowns

n = getIntGreaterThan1("Enter the no. of unknowns: ")
a, b, c, u = [0], [], [], []
for i in range(n):
    if i != 0:
        a.append(getFloat("Enter the value of a"+(str)(i+1)+": "))
    b.append(getFloat("Enter the value of b"+(str)(i+1)+": "))
    if i != n-1:
        c.append(getFloat("Enter the value of c"+(str)(i+1)+": "))
    u.append(getFloat("Enter the value of u"+(str)(i+1)+": "))
c.append(0)
print("\nSolution for given linear equations:")
print(getUnknowns())
'''
n = 6
a = [0.0, 3.0, 4.0,  1.0, 1.0, -1.0]
b = [1.0, 2.0, 1.0,  2.0, 5.0, 2.0]
c = [2.0, 3.0, 6.0,  3.0, 6.0, 0.0]
u = [1.0, 3.0, 9.0, -3.0, 2.0, 5.0]
[-9.125   5.0625  6.75   -3.     -1.25    1.875 ]
'''