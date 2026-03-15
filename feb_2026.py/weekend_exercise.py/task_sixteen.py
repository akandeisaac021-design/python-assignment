name =input("Enter your name: ")
digit =0

for letter in name:
    if (letter.lower() =="a" or letter.lower() =="e" or letter.lower() =="i" or letter.lower() =="o" or letter.lower() =="u"):
        digit +=1

print(digit)
