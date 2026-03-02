number = int(input("Enter a number: "))
result = 0 


if number <= 1:
    print(f"{number} is not prime")
else:
    
    for divisor in range(2, number): 
        if (number % divisor== 0):
            result += 1 
            break 


    if (result == 0):

        print(f"{number} is prime")
    else: 

        print(f"{number} is not prime")


