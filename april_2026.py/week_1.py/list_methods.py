#1. Given a list of numbers, write a python function using map () that squares each number in the list 
#1-2-3-4-5
#1-4-9-16-25
#
#2. write a python function that converts a list of strings to their corresponding length using the map() function
#3. write a python function using filter() that returns a list of all the even numbers from a given list of integers
#4. Using filter(), create a python function that filters out all the words with morenthan 5 characters from the following list.
#5. using reduce(), write a python function to concatenate all strings in a list into a string add an hyphen in between each string
numbers =[1, 2, 3, 4, 5]


def square_of_numbers(value):

    result =value **2

    return result

#print(square_of_numbers(numbers))
print(list(map(square_of_numbers, numbers)))
#

names =["my", "name", "is", "isaacA"]
def length_of_each_string_in_a_list(name):
    return len(name)

print(list(map(length_of_each_string_in_a_list,  names)))

def even_numbers(number):
    
    return number % 2 ==0

print(list(filter(even_numbers, numbers)))

def words_greater_than_5_characters(name):

    return len(name) >5

print(list(filter(words_greater_than_5_characters, names)))

from functools import reduce

def string_combiner(name1, name2):

    new_name =name1 + "-" +name2

    return new_name

print(list(reduce(string_combiner, names)))

#filtered_iterable =filter(1, numbers)
#for number in str(filtered_iterable):
#    print(number)
#
#
#print(filtered_iterable)
