import random

def string_pattern():

    alphabets ="qwertyuioplkjhgfdsazxcvbnm"

    random_index =random.randint(50)

    print(f"{alphabets[random_index].upper()}"*3, f"{random_index}"*3, f"{alphabets[(random_index*2) % 26]}", f"{alphabets[(random_index*3) % 26]}", end="-")

def text_index_search_tool(target):
    text = "my name isaac"

    indexes = []

    for index, letter in enumerate(text):
        if letter == target:
            indexes.append(index)
    return tuple(indexes)


