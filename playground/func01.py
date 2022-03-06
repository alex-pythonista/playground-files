# with parameters and with return values
def even_or_odd(num):

    if num%2 == 0:
        return "Even"
    else: 
        return "Odd"

def add(x, y): 
    return x+y

def magicNumber(name):

    l = len(name)
    mn = add(l, 3)
    return




number = int(input("Enter a number: "))

result = even_or_odd(number)

print("Given number is " + result)