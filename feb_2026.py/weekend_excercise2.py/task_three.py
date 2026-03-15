name =input("Enter your name: ")
count =0

for letter in name:
    if (letter.isupper()):
        count +=1 
print(count)       
