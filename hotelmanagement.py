# Hotel Management System in Python

class HotelManagementSystem:
    def __init__(self):
        self.rooms = {
            "Single": {"price": 1570, "available": 10},
            "Double": {"price": 2500, "available": 10},
            "Suite": {"price": 4500, "available": 5},
        }
        self.customers = []

    def display_rooms(self):
        print("\nRoom Types Available:")
        for room_type, details in self.rooms.items():
            print(f"{room_type}: ₹{details['price']} per night - {details['available']} available")

    def book_room(self):
        name = input("Enter customer name: ")
        room_type = input("Enter room type (Single, Double, Suite): ")
        nights = int(input("Enter number of nights: "))

        if room_type not in self.rooms:
            print("Invalid room type. Please try again.")
            return

        if self.rooms[room_type]["available"] > 0:
            self.rooms[room_type]["available"] -= 1
            cost = self.rooms[room_type]["price"] * nights
            self.customers.append({
                "name": name,
                "room_type": room_type,
                "nights": nights,
                "total_cost": cost
            })
            print(f"Room booked successfully for {name}. Total cost: ₹{cost}")
        else:
            print(f"Sorry, no {room_type} rooms are available.")

    def checkout(self):
        name = input("Enter customer name for checkout: ")
        for customer in self.customers:
            if customer["name"] == name:
                print(f"Checking out {name}. Total bill: ₹{customer['total_cost']}")
                self.customers.remove(customer)
                self.rooms[customer["room_type"]]["available"] += 1
                return
        print(f"No customer found with the name {name}.")

    def show_customers(self):
        if not self.customers:
            print("No customers at the moment.")
        else:
            print("\nList of current customers:")
            for customer in self.customers:
                print(f"{customer['name']} - {customer['room_type']} room for {customer['nights']} night(s), Total: ₹{customer['total_cost']}")

def main():
    system = HotelManagementSystem()
    
    while True:
        print("\n--- Hotel Management System ---")
        print("1. Display Room Information")
        print("2. Book a Room")
        print("3. Checkout")
        print("4. View Current Customers")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.display_rooms()
        elif choice == "2":
            system.book_room()
        elif choice == "3":
            system.checkout()
        elif choice == "4":
            system.show_customers()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
