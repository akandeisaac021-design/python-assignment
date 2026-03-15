def odd_words_collector():
    word =input("Enter a word: ")
    word_length =len(word)
    letters =list(word)
    counter =0
    new_word =" "
    while (counter <= word_length):
        letter =letters[counter]
        if (counter % 2 == 1):
            new_word +=letter
        counter +=1
