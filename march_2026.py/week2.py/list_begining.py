numbers =[2, 5, 7, 1, 6, 9]

def integer_list_sorter(numbers):

    temporary_space=0

    for index in range(0, len(numbers)):

        for index2 in range(0, len(numbers)):

            if (numbers[index] <numbers[index2]):

                temporary_space =numbers[index]
                numbers[index] =numbers[index2]
                numbers[index2] =temporary_space

    return numbers



def even_numbers_list(numbers):

    even_numbers_list =[]

    for index in range (0,len(numbers)):

        if (numbers[index] %2 ==0): even_numbers_list.append(numbers[index])

    return even_numbers_list



def list_combining_function(first_list, second_list):

    combination_list =[]
    
    for index in range(0, len(first_list)): combination_list.append(first_list[index])
        
    for index in range(0, len(second_list)):    combination_list.append(second_list[index])    

    integer_list_sorter(combination_list)

    new_list =f"first_list + second_list"

    return integer_list_sorter


def function_to_return_strings_with_3_and_above_characters(string_list):
    list_of_strings_greater_than_3 =[]

    for _ in range(0, len(list_of_strings_greater_than_3)):

        if (len(string_list[index]) >3):    list_of_strings_greater_than_3.append(string_list[index])

        return list_of_strings_greater_than_3


def pseudo_range(numbers):

    integer_list_sorter(numbers)

    pseudo_range =numbers[-2] -numbers[1]

    return pseudo_range
