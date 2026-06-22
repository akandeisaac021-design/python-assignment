from fuel import Fuel


class Dispenser:
    def __init__(self):
        self.inventory = {}  # Dictionary collection of Fuel: {fuel_name: Fuel object}

    def add_fuel(self, fuel: Fuel):
        if fuel.fuel_name in self.inventory:
            print (f"{fuel.fuel_name} already exists in the dispenser.")
            return;
        self.inventory[fuel.fuel_name] = fuel

    def get_fuel(self, fuel_name: str) -> Fuel:
        if fuel_name not in self.inventory:
            print(f"Fuel type '{fuel_name}' is not available.")
            return;
        return self.inventory[fuel_name]