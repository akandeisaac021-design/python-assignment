weight =int(input("Enter your weight: "))
height =int(input("Enter your height: "))
height_sqr =height * height
bmi =weight/height_sqr
if (bmi<18.5):
    print("Underweight")
elif (bmi>=18.5 and bmi<=24.9):
    print("Normal")
elif (bmi>=25 and bmi>=29.9)
    print("Overweight")
elif (bmi>=30):
    print("Obese")
