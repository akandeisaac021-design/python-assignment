number =4
multiple =1


while (multiple < 11):
    multiplication =number * multiple
    multiple +=1
    new_multiple =1
    print("multiples of " + str(multiplication) + ":") 
    while (new_multiple <6):
        new_multiplication =multiplication * new_multiple
        new_multiple +=1
        print(new_multiplication)
