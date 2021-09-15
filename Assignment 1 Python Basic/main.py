import random;

def getIntGreaterThan1(inputText):
    while True:
        try:
            n = int(input(inputText));
            if(n >= 1):
                return n
            else:
                raise Exception()
        except:
            print("Invalid Input. Expected inpur: Integer greater than 0")

def getInt(inputText):
    while True:
        try:
            return int(input(inputText))
        except:
            print("Invalid Input. Expected inpur: Integer")
    
def getFactorial(n):
    if(n == 1):
        return 1;
    else:
        return n * getFactorial(n-1);

def factorialPart():
    print("Factorial: ", getFactorial(getIntGreaterThan1("Enter the number whose factorial is required: ")));

def Reverse(lst):
    return [ele for ele in reversed(lst)];

def listReversalPart():
    list1 = [];
    for i in range(getIntGreaterThan1("Enter the number of int in the list: ")):
        list1.append(getInt("Enter int " + str(i+1) + ": "));
    reversedList = Reverse(list1);
    print("Given List:", list1)
    print("Reversed List:", reversedList);
    
def randomNumberGenerationPart():
    for i in range(getIntGreaterThan1("Enter the number of random numbers to be generated: ")):
        print("Random number", i+1, ":", random.random())
      
factorialPart();
listReversalPart();
randomNumberGenerationPart();