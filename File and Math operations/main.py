import random
import csv
import math
import pandas as pd
from matplotlib import pyplot as plt

#get f(x)
def f(x):
    return x * math.cos(x-4)

#Get 100 random number and their f(x)
list1 = []
for i in range(100):
    x = random.uniform(-10, 10)
    list1.append([x, f(x)])

#write in csv file
fields = ['x', 'y']
filename = "C:\\Users\Raider\\Downloads\\IIT ISM Dhanbad\\Sem 1\\Practicals\\Computer Oriented Numerical Methods-Practical\\Assignment 2\\records.csv"
with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(list1)

#read and plot them
df = pd.read_csv(filename)
plt.scatter(df[['x']], df[['y']])
