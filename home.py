# to take only even index characters
x = input('Enter a string: ')
new_str = ""
for i in x:
    if x.index(i)%2 != 0:
        new_str += i

# converting them from lowercase to uppercase
i = 0
up_str = ""
while len(new_str) > i:
    if new_str[i]>='a' and new_str[i]<='z':
        up_str+=chr(ord(new_str[i])-32)
    else:
        up_str += chr(ord(new_str[i]))
    i+=1
print("Uppercase string is:", up_str)