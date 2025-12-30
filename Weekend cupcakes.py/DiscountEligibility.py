total_bill =int(input("Enter your Tota bill: "))
is_member =char(input("Do you have Membership(Y/N): "))

if (is_member ==Y and total_bill>=1000):
    print('10% off')
elif (is_member ==N and total_bill>=1000):
    print("5%")
else:
    print(total_bill)
