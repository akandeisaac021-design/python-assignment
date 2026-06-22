class Fuel:

    def __init__(self, fuel_name: str, price_per_liter: float, quantity: float):
        self.fuel_name = fuel_name
        self.price_per_liter = price_per_liter
        self.quantity = quantity


    def reduce_stock(self, liters: float):
        if liters > self.quantity:
            print(f"Insufficient stock! Only {self.quantity:.2f}L left.")
            return;
        self.quantity -= liters


    def add_stock(self, liters: float):
        if liters <= 0:
            print("Restock quantity must be positive.")
            return;
        self.quantity += liters


    def update_price(self, new_price: float):
        if new_price <= 0:
            print("Price per liter must be greater than zero.")
            return;
        self.price_per_liter = new_price