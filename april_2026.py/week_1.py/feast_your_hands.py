def str_to_int_converter(string):
    return int(string)

strings =["1", "2", "3", "4", "5", "6", "7", "9", "10"]
numbers =list(map(str_to_int_converter, strings))

print(numbers)
print(sum(numbers))

def farenheit_to_celsius_converter(celcius):

    return f"{celcius * 9/5 +35}*C"

print(list(map(farenheit_to_celsius_converter, numbers)))

list_of_object =["Isaac", None, 67, True, 54.5, None]

def None_values_remover(value):

    return value != None
        
print(list(filter(None_values_remover, list_of_object)))

numbers =[1, 3, 4, 6, 9, 12]

def numbers_divisible_by_three(number):
    
    return number % 3 ==0

print(list(filter(numbers_divisible_by_three, numbers)))

numbers =[-2, -1, 0, 1, 2]

def positive_numbers_filter(number):

    return number >-1

print(list(filter(positive_numbers_filter, numbers)))

from functools import reduce

numbers =["2", "3", "4"]

def product_of_a_list_of_number(number1, number2):

    product =int(number1) * int(number2)

    return str(product)

def high_value_numbers(number1, number2):

    if int(number1) > int(number2) :
        return str(number1)
    else:
        return str(number2)

print(list(reduce(high_value_numbers, numbers)))

new_string =""
for digit in list(reduce(product_of_a_list_of_number, numbers)):
    new_string +=digit

new_string =int(new_string)

print(new_string)

names =["me", "and", "you"]
def string_combiner(name1, name2):

    new_name =name1 + name2

    return new_name

print(list(reduce(string_combiner, names)))
