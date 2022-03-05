# with parameters and with return values
def even_or_odd(num):

    if num%2 == 0:
        return "Even"
    else: 
        return "Odd"


number = int(input("Enter a number: "))

result = even_or_odd(number)

print("Given number is " + result)