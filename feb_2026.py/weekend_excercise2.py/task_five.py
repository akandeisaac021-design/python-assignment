name =input("Enter your name: ")
index =0

for letter in name.lower():
    if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
        print (index +1)
        break
    index +=1
