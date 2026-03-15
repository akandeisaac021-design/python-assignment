def temperature_converter(celsius):
#    convert from celsius to pareheit
    farenheit =( celsius * (9/5) ) + 32;

    return farenheit


#===========================================
def calculate_factorial(number):
    multiplier =number -1
    factorial =1

    while (multiplier >1):
        factorial *=multiplier
        multiplier -=1

    return factorial

#============================================

import random

def guess_game(number):

    random_number =random.randint(1, number)

    guessed_number =int(input(f"Guess a number from 1 to {number} ->"))

    count =2

    while (random_number != guessed_number):

        guessed_number =int(input(f"Try again to guess a number from 1 to {number} ->")) 
        
        if (count >=3):
            random_number =random.randint(1, number)
            print ("Random number has been altered")
            count =0

        count +=1

number =int(input("Enter a number for your guess range ->"))
guess_game(number)







