import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values
a = 1
b = 1/math.sqrt(2)
p = 1
t = 1/4


# perform 10 iterations of this loop
for i in range(1, 10):

    a1 = (a+b)/2
    b1= math.sqrt(a*b)
    p1 = 2 * p
    t1= t - p*(math.pow(a1-a,2))
    a = a1
    b = b1
    p = p1
    t= t1

    pi_estimate = math.pow(a1 + b1,2)/(4*t1)

    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """

    ### YOUR CODE HERE ###

# print out the current loop iteration. This is present to have something in the loop.
print("Loop Iteration: ", i)

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# modify this line below to estimate PI

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))
