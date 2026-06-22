
def prime_values(numbers):
    
    new_numbers =[]
    for number in numbers:
        count =0
        for factor in range(2,number):
            if number % factor ==0:
                count +=1
        if count ==0:
            new_numbers.append(number)

    return set(new_numbers)
numbers =[1,2,3,4,5,6,7,8,9,10]
print(prime_values(numbers))
