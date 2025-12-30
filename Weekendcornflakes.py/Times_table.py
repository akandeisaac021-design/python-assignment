multiple =int(input("Enter a multiple:"))

for number in range(1, 16):
    print(f"{number} * {multiple}  ={"":>5} {number * multiple}")
