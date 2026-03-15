binary =input("Enter a binary number: ") 
length =len(binary)
decimal =0
base =2

for digit in binary:
    decimal +=int(digit) * (base **(length-1))
    length -=1

print (decimal)
