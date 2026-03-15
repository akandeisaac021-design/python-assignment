def word_creator():
    first_word =input("Enter first word: ")
    if (len(first_word) <2):
        first_letter =""   
    elif (len(first_word) >=2):
        first_word_letters =list(first_word)    
        first_letter =first_word_letters[0]
        second_letter =first_word_letters[1]
        last_letter =first_word_letters[-1]
        second_to_last_letter =first_word_letters[-2]

    return (first_letter + second_letter + second_to_last_letter + last_letter)
    
