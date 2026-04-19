#import random
#
#def random_integer_list_function():
#    numbers =[random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50), random.randint(1, 50)]
#
#    return numbers;
#
#
#def list_length_function(numbers):
#    length =0
#    for _ in numbers:
#        length +=1
#
#    return length;        
#
#
#def sum_of_even_indexes_in_a_collection(numbers):
#    sum_of_numbers_at_even_index =0
#    for index in range(0, length_function(numbers), 2):
#         sum_of_numbers_at_even_index +=numbers[index]
#
#    return sum_of_numbers_at_even_index
#
#
#def sum_of_odd_indexes_in_a_collection(numbers):
#    sum_of_numbers_at_odd_index =0
#    for index in range(1, length_function(numbers), 3):
#         sum_of_numbers_at_odd_index +=numbers[index]
#
#    return sum_of_numbers_at_odd_index
#
#def multiple_of_every_third_index(numbers):
#    multiple_of_numbers_at_every_third_index =1
#    for index in range(3, length_function(numbers), 3):
#         multiple_of_numbers_at_every_third_index *=numbers[index]
#
#    return multiple_of_numbers_at_every_third_index
#
#def average_of_a_list(numbers): 
#    return sum(numbers) / length_function(numbers)
#
#
#def integer_list_sorter(numbers):
#    temporary_space=0
#
#    for index_number_currently_being_compared in range(0, length_function(numbers)):
#        for index_of_numbers_to_compare_with in range(0, len(numbers)):
#            if (numbers[index_number_currently_being_compared] <numbers[index2]):
#
#                temporary_space =numbers[index_number_currently_being_compared]
#                numbers[index_number_currently_being_compared] =numbers[index_of_numbers_to_compare_with]
#                numbers[index_of_numbers_to_compare_with] =temporary_space
#    return numbers
#
#def highest_number_in_a_list(numbers):
#    integer_list_sorter(numbers)
#    return numbers[-1]
#
#def lowest_number_in_a_list(numbers):
#    integer_list_sorter(numbers)
#    return numbers[0]
#
#
#def function_to_return_strings_with_length_greater_than_two_and_the_same_letter_starting_and_ending_them(names):
#    length = length_function(names)
#    count =0
#    new_name =[]
#
#    for name in names:
#        name =name.lower()
#        if (length_function(name) >2 and name[1] == name[-1]):
#            new_names.append(count)
#            count +=1
#
#    return new_names
#
#
#def list_of_random_sequential_integers_from_one_to_fifteen():
#    numbers =[] 
#    for _ in range(0, 10):
#        random_number =random.randint(1, 15)
#        numbers.append(random_number)
#
#    return numbers
#
#
#def sum_of_every_third_index(numbers):
#    sum_of_numbers_at_every_third_index =0
#
#    for index in range(3, length_function(numbers), 3):
#         sum_of_numbers_at_every_third_index +=numbers[index]
#
#    return sum_of_numbers_at_every_third_index
#
#
#def sum_of_first_last_and_middle_numbers_in_a_list(numbers):
#    middle_index =0
#
#    if (len(numbers) %2 ==1):
#        middle_index =len(numbers) //2
#    else:
#        first_middle_index =len(numbers) //2
#        second_middle_index =(len(numbers) //2) + 1
#        true_middle_index =(first_middle_index + second_middle_index) /2
#    
#    return numbers[0] + middle_index + numbers[-1]

print(help(sorted))
