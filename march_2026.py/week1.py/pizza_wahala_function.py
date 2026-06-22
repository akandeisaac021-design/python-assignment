print("Welcome to Newtons one-stop pitza store !!!")

pizza_menu = {
    "Sapa Size": (4, 2000),
    "Small Money": (6, 2400),
    "Big Boys": (8, 3000),
    "Odogwu": (12, 4200)
}

number_of_guests = int(input("Enter number of guests: "))

print("""
    Would you like Sapa Size, 
                   Small Money, 
                   Big Boys, 
                   Odogwu""")

pizza_type = input("Enter the pizza type you want: ")
pizza_type.title()

if pizza_type in pizza_menu:
    slices_per_box, price_per_box = pizza_menu[pizza_type]

    number_of_boxes = number_of_guests // slices_per_box

    if number_of_guests % slices_per_box != 0:
        number_of_boxes += 1

    total_slices = number_of_boxes * slices_per_box
    leftover_slices = total_slices - number_of_guests

    total_price = number_of_boxes * price_per_box

    print("\nOrder Summary:")
    print(f"Number of boxes of pizza to buy = {number_of_boxes} boxes")
    print(f"Number of leftover slices = {leftover_slices} slices")
    print(f"Total price = ₦{total_price}")

else:
    print("Error: The pizza is not on the menu.")
