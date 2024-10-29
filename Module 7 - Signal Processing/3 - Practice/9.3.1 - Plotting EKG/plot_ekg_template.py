
import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy

path = '../../../data/ekg/mitdb_201.csv'
# load data in matrix from CSV file; skip first two rows
data= np.loadtxt(path,delimiter=',',skiprows=2)

# save each vector as own variable
First = []
Second =[]
Third =[]

First = data[:,0]
Second = data[:,1]
Third = data[:,2]

# use matplot lib to generate a single
plt.plot(First,Second)
plt.plot(First,Third)
plt.title("MLII & V1 over Time")
plt.xlabel("Time")
plt.ylabel("MLII & V1")
plt.show()