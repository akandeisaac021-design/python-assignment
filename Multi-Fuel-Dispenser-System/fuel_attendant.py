import datetime

from dispenser import Dispenser
from fuel import Fuel


class FuelAttendant:

    def __init__(self, full_name: str, dispenser: Dispenser):
        self.full_name = full_name
        self.dispenser = dispenser
        self.transactions = []


    def setup_new_fuel(self, name: str, price: float, initial_qty: float):
        new_fuel = Fuel(name, price, initial_qty)
        self.dispenser.add_fuel(new_fuel)

    def view_available_fuel(self) -> dict:
        return {
            name: {"price": f"₦{fuel.price_per_liter}", "stock": f"{fuel.quantity}L"}
            for name, fuel in self.dispenser.inventory.items()
        }

    def update_fuel_price(self, fuel_name: str, new_price: float):
        fuel = self.dispenser.get_fuel(fuel_name)
        fuel.update_price(new_price)

    def restock_fuel(self, fuel_name: str, liters: float):
        fuel = self.dispenser.get_fuel(fuel_name)
        fuel.add_stock(liters)

    def dispense_by_liters(self, fuel_name: str, liters: float) -> dict:

        if not (1 <= liters <= 50):
            print("Liters bought must be between 1 and 50 liters.")
            return None;

        fuel = self.dispenser.get_fuel(fuel_name)
        fuel.reduce_stock(liters)

        total_cost = liters * fuel.price_per_liter
        return self._record_and_generate_receipt(fuel_name, liters, total_cost, "Liters")

    def dispense_by_amount(self, fuel_name: str, amount_paid: float) -> dict:
        fuel = self.dispenser.get_fuel(fuel_name)

        if amount_paid <= fuel.price_per_liter:
            print(f"Amount must be above the price of a single liter (₦{fuel.price_per_liter}).")
            return None;

        calculated_liters = amount_paid / fuel.price_per_liter
        fuel.reduce_stock(calculated_liters)

        return self._record_and_generate_receipt(fuel_name, calculated_liters, amount_paid, "Amount")

    def _record_and_generate_receipt(self, fuel_name: str, liters: float, cost: float, mode: str) -> dict:
        receipt = {
            "transaction_id": len(self.transactions) + 1,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "attendant": self.full_name,
            "fuel_type": fuel_name,
            "dispense_mode": mode,
            "liters_delivered": round(liters, 2),
            "total_amount": round(cost, 2)
        }
        self.transactions.append(receipt)
        return receipt

    def show_all_transactions(self) -> list:
        return self.transactions
