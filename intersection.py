# given 2 arrays locate the matching numbers that are on array1 and array2

# def intersection(arr1, arr2):
#     # iterate on arr1
#     for i in arr1:
#         # iterate on arr2
#         for j in arr2:
#             # compare each item of both array
#             if i == j:
#                 print(i)

# intersection([1,6,8,9,3], [6,3,6,7,1])

# O(i*j)  i==j==n  O(n^2)
# quadratic complexity

# O(1) Constant once quick = quick
# O(log n) Log
# O(n) Linear
# O(n log n) Log Linear
# O(n^2) Quadratic
# O(k^n) Exponential = super long

def inter(arr1, arr2):
    new_list=[]
    arr1.sort()  # O(a log a) Log Linear
    arr2.sort()  # O(b log b) Log Linear
    for i in arr1:
        if i in arr2:
            new_list.append(i)
    # Time complexity is O(a+b) = O(n)

    print(new_list)

inter([1,6,8,9,3], [6,3,6,7,1])

