# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20 , print Not Weird

def odd_num(n):
    if n % 2 != 0:
        print("Weird")

    elif n % 2 == 0 and 2<=n<=5:
        print("Not Weird")

    elif n % 2 == 0 and 6<=n<=21:
        print("Weird")

    elif n % 2 == 0 and 20<=n:
        print("Not Weird")

# output s/b Weird
# odd_num(3)

# output s/b Not Weird
odd_num(24)
