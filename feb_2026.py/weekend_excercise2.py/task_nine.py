number =int(input("Enter a number: "))

start =1
stop =number + 1
count =0

while (start <stop):
    if (number % start ==0):
        count +=1
    start +=1
print(count)
