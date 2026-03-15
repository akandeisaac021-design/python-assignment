number =int(input("Enter a number: "))

start =1
stop =number + 1

while (start <stop):
    if (number % start ==0):
        print(start)
    start +=1
