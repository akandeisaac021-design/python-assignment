multiple =1
number =4

sum_of_the_multiples_of =1


while (multiple < 11):
    multiplication =number * multiple
    multiple +=1
    new_multiple =1
    sum_of_new_multiples =0

    while (new_multiple <6):
        new_multiplication =multiplication * new_multiple
        new_multiple +=1
        sum_of_new_multiples +=new_multiplication
        if (new_multiple > 5):
            print("The sum of the multiples of the of the multiples of "+ str(sum_of_the_multiples_of) + " is : " +  str(sum_of_new_multiples))
        
