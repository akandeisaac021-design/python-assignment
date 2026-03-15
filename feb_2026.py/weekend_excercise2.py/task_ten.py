number =int(input("Enter a number: "))
number =str(number)
reversed_string =reversed(str(number))
new_string =""

for digit in reversed_string:
    new_string +=f"{digit}"
    print(new_string)
if (number == new_string):
    print("it is a palindrome")
else:
    print("it is not a palindrome")
