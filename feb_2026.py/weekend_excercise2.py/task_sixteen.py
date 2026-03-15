start =1
count =0

while (start <101):
    divisor =1
    while (divisor <start):
        if (start % divisor ==0):
            count +=1
        divisor +=1
    if (count >2):
        "nothing to see here"
    else:
        print(f"{start} is a prime number")
    count =0
    start +=1
