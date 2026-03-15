multiple =1
number =4

sum_of_the_pair_in_task_seven =0
while (multiple < 11):
    multiplication =number * multiple
    multiple +=1
    new_multiple =1
    sum_of_new_multiples =0

    while (new_multiple <6):
        new_multiplication =multiplication * new_multiple
        new_multiple +=1
        sum_of_new_multiples +=new_multiplication
    sum_of_the_pair_in_task_seven +=sum_of_new_multiples
square_of_the_sum_of_the_pair_in_task_seven =sum_of_the_pair_in_task_seven * sum_of_the_pair_in_task_seven
print("The sum of the pair in task seven is : " + str(square_of_the_sum_of_the_pair_in_task_seven))

        
