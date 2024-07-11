# 12345_q3.py
class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        for vehicle in self.vehicles:
            if isinstance(vehicle, Car):
                print(f"Car: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Seats: {vehicle.number_of_seats}")
            elif isinstance(vehicle, Truck):
                print(f"Truck: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Cargo Capacity: {vehicle.cargo_capacity}")
            elif isinstance(vehicle, Motorcycle):
                print(f"Motorcycle: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Engine Capacity: {vehicle.engine_capacity}")

    def search_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                if isinstance(vehicle, Car):
                    print(f"Found Car: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Seats: {vehicle.number_of_seats}")
                elif isinstance(vehicle, Truck):
                    print(f"Found Truck: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Cargo Capacity: {vehicle.cargo_capacity}")
                elif isinstance(vehicle, Motorcycle):
                    print(f"Found Motorcycle: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Engine Capacity: {vehicle.engine_capacity}")
                return
        print(f"Vehicle with registration number {registration_number} not found.")

def main():
    fleet = Fleet()

    while True:
        print("\nMenu:")
        print("1. Add Vehicle")
        print("2. Display All Vehicles")
        print("3. Search Vehicle by Registration Number")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            type_of_vehicle = input("Enter type of vehicle (Car/Truck/Motorcycle): ").lower()
            registration_number = input("Enter registration number: ")
            make = input("Enter make: ")
            model = input("Enter model: ")

            if type_of_vehicle == 'car':
                number_of_seats = int(input("Enter number of seats: "))
                vehicle = Car(registration_number, make, model, number_of_seats)
            elif type_of_vehicle == 'truck':
                cargo_capacity = float(input("Enter cargo capacity: "))
                vehicle = Truck(registration_number, make, model, cargo_capacity)
            elif type_of_vehicle == 'motorcycle':
                engine_capacity = float(input("Enter engine capacity: "))
                vehicle = Motorcycle(registration_number, make, model, engine_capacity)
            else:
                print("Invalid vehicle type.")
                continue

            fleet.add_vehicle(vehicle)
        elif choice == 2:
            fleet.display_vehicles()
        elif choice == 3:
            registration_number = input("Enter registration number to search: ")
            fleet.search_vehicle(registration_number)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
