start =1
count =0
prime_number_counter =0

while (start <101):
    divisor =1

    while (divisor <start):

        if (start % divisor ==0):
            count +=1
        divisor +=1

    if (count >2):
        "nothing to see here"
    else:
        prime_number_counter +=1
    count =0
    start +=1

print(f"there are {prime_number_counter} prime numbers")
