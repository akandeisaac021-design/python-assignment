def length_of_set(numbers):
    count =0

    set_of_values =set(numbers)

    for _ in set_of_values:
        count +=1

    length =count

    return length;  
numbers =[1,2,3,4,5,6,7,8,9,10]
print(length_of_set(numbers))
