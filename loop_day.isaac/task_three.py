positive_integer =int(input("Enter a positive integer: "))
count =0

while (positive_integer <=0):
    positive_integer =int(input("Enter a positive integer: "))

while (positive_integer >1):
    if (positive_integer %2 ==0):
        positive_integer /=2
    else:
        positive_integer /=3
        positive_integer +=1
    count +=1
print(f"It took {count} steps to reach 1")

