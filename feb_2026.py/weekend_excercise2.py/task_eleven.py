name =input("Enter a name: ")
name =str(name)
reversed_string =reversed(str(name))
new_string =""

for letter in reversed_string:
    new_string +=f"{letter}"
    print(new_string)
if (name == new_string):
    print("it is a palindrome")
else:
    print("it is not a palindrome")
