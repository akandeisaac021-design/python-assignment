decimal =int(input("Enter a number: "))

base =2

result =0

new_string =""

while (result !=0):
    result =decimal / base
    print(result)
    remainder =decimal % base
    new_string +=str(remainder)
    print(new_string)

#for digit in reversed(new_string):
#    print(digit, end=" ")
