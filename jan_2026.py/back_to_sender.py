import unittest

print("Back TO Sender LLC")

successful_deliveries =int(input("Enter your Successful: "))
while (successful_deliveries <0 or successful_deliveries >100):
    print("Re-enter a valid number")
    successful_deliveries =int(input("Enter your Successful: "))
base_pay =5000

def days_wage_function(successful_deliveries):

    if (successful_deliveries < 50):
        amount_per_parcel =160

    elif(successful_deliveries >=50 and successful_deliveries <=59):
        amount_per_parcel =200

    elif(successful_deliveries >=60 and successful_deliveries <=69):
        amount_per_parcel =250

    elif(successful_deliveries >=70):
        amount_per_parcel =500

    days_wage =successful_deliveries * amount_per_parcel + base_pay
    return days_wage
payment =days_wage_function(successful_deliveries)
print("Today's wage is : ", days_wage_function(successful_deliveries))


class test_days_wage_function(unittest.TestCase):

    def test_less_than_50(self):

        for delivery in range(0,50):
            testing =delivery *160 +5000
            self.assertEqual(days_wage_function(delivery), testing)

    def test_from_50_to_59(self):

        for delivery in range (50, 60):
            testing =delivery *200 +5000
            self.assertEqual(days_wage_function(delivery), testing)

    def test_from_60_to_69(self):

        for delivery in range(60, 70):
            testing =delivery *250 +5000
            self.assertEqual(days_wage_function(delivery), testing)

    def test_from_70_to_hundred(self):

        for delivery in range(70, 101):
            testing =delivery *500 +5000
            self.assertEqual(days_wage_function(delivery), testing)





if __name__=="_main_":
    unittest.main()
