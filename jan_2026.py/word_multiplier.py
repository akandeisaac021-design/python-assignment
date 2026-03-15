word =input("Enter your word: ")
multiple =int(input("Enter a multiple: "))


counter =0

new_word =" " 

word_letters=list(word)
word_letters_length=len(word_letters)

total_expected_letters =word_letters_length * multiple

while(counter < word_letters_length):
    new_word =new_word + word_letters[counter]
    new_word_length =len(new_word)
    counter +=1

    if (counter >= word_letters_length):
        counter =0
    if (new_word_length > total_expected_letters ):
        break
print(new_word)
