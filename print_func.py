# Read an integer N .
# Without using any string methods, try to print the following:
# 123...N
# Note that "..." represents the values in between.
# Input Format
# The first line contains an integer N.
# Output Format
# Output the answer as explained in the task.
# Sample Input 0
# 3
# Sample Output 0
# 123

def print_num(n):
    for i in range(n):
        i+=1
        print(i, end="")

print_num(3)