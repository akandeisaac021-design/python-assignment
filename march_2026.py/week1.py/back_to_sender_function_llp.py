def amount_per_parcel_function(successful_deliveries):
    if (successful_deliveries <50):

         amount_per_parcel =160

    elif (successful_deliveries >49 and successful_deliveries <60):

        amount_per_parcel =200

    elif (successful_deliveries >59 and successful_deliveries <70):

        amount_per_parcel =250


    else:
        amount_per_parcel =500

    return amount_per_parcel
    
def days_wage_function(successful_deliveries):
    base_pay =5000

    days_wage =successful_deliveries * amount_per_parcel_function(successful_deliveries) + base_pay

    return days_wage

successful_deliveries =int(input("Enter amount of packages delivered: "))
amount_per_parcel_function(successful_deliveries)
days_wage_function(successful_deliveries)
print(f"You have made ${days_wage_function(successful_deliveries)} today")
