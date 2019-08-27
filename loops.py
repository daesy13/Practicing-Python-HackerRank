# Task
# Read an integer N. For all non-negative integers i<N , print i^2. See the sample for details.

# Input Format
# 5

# Output Format
# 0
# 1
# 4
# 9
# 16

# The first and only line contains the integer, N.

def square(n):
    for i in range(0,n):
        print(i*i)

square(5)