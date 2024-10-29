import matplotlib.pyplot as plt
import numpy as np
import scipy
import math

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

signal = 0
## YOUR CODE HERE ##
signal = np.loadtxt(signal_filepath,delimiter=',',skiprows=2)
plt.title('Process Signal for ' + database_name)
plt.plot(signal)
plt.show()

Time = signal[:,0]
ML2 = signal[:,1]
V1 = signal[:,2]
"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##
 ## filtered_signal = scipy.signal.butter()
"""
Step 3: Pass data through weighted differentiator
"""
## YOUR CODE HERE ##
mag_Time = np.sqrt(Time**2)
mag_ML2 = np.sqrt(ML2**2)
mag_V1 = np.sqrt(V1**2)
diff_Time = np.diff(mag_Time)
diff_ML2 = np.diff(mag_ML2)
diff_V1 = np.diff(mag_V1)

plt.title('Difference Signal')
plt.plot(diff_V1)
plt.xlabel('Time')
plt.ylabel('Difference of V1')
plt.show()
"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##
square_Time = pow(diff_Time,2)
square_ML2 = pow(diff_ML2,2)
square_V1 = pow(diff_V1,2)

plt.title('Squared signal')
plt.plot(square_V1)
plt.xlabel('Time')
plt.ylabel('Square of V1')
plt.show()
"""
Step 5: Pass a moving filter over your data
"""
## YOUR CODE HERE
comparison = np.ones(5)
moving_average_ML2 = np.convolve(square_ML2,comparison)
moving_average_V1 = np.convolve(square_V1, comparison)

plt.title('Moving average of signal')
plt.plot(moving_average_V1)
plt.xlabel('Time')
plt.ylabel('Moving average of V1')
plt.show()
# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
