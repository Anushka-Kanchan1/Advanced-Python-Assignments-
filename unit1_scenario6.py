class Vehicle:
    def __init__(self, number, brand, price):
        self.number = number
        self.brand = brand
        self.price = price

    def category(self):
        return "Luxury" if self.price >= 1000000 else "Economy"

    def display(self):
        print(f"{self.number} | {self.brand} | ₹{self.price} | {self.category()}")


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_all(self):
        print("\n--- Vehicle Showroom ---")
        for vehicle in self.vehicles:
            vehicle.display()


# Creating objects
showroom = Showroom()

v1 = Vehicle("MH12AB1234", "Toyota", 800000)
v2 = Vehicle("MH14CD5678", "BMW", 2500000)
v3 = Vehicle("MH15EF9012", "Honda", 1200000)

# Adding vehicles
showroom.add_vehicle(v1)
showroom.add_vehicle(v2)
showroom.add_vehicle(v3)

# Display all vehicles
showroom.display_all()


OUTPUT 

--- Vehicle Showroom ---
MH12AB1234 | Toyota | ₹800000 | Economy
MH14CD5678 | BMW | ₹2500000 | Luxury
MH15EF9012 | Honda | ₹1200000 | Luxury
