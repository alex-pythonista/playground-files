import functools
lst = [3, 6, 5, 9, 2]
 
# total function
def total(x, y):
    return x+y

# using reduce to compute sum of list
result = functools.reduce(total, lst)

print("The sum of the list elements is : ", result)