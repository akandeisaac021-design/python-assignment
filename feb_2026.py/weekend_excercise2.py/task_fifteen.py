number =int(input("Enter a number: "))
number =str(number)
add_even =0

for digit in number:
    if (int(digit) % 2 ==1):
        add_even +=1
print(add_even)
