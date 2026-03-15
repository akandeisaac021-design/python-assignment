principle =int(input("Enter your principle: "))
annual_interest =int(input("Enter your annual interest: "))
duration =int(input("Enter your duration: "))
annual_rate =int(input("Enter your rate: "))
monthly_rate =(rate / 100) /12

numerator =monthly_rate*( 1 + monthly_rate)**duration
denominator =(annual_interest + monthly_rate )**duration -1

monthly_payment_value =principle * numerator / denominator

float(monthly_payment_value)
print(monthly_payment_value)
