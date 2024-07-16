class PharmacyManagementSystem:
    def __init__(self):
        self.medicines = {}

    def add_medicine(self, name, quantity):
        if name in self.medicines:
            print("Medicine already exists. Updating quantity...")
            self.medicines[name] += quantity
        else:
            self.medicines[name] = quantity
            print("Medicine added successfully.")

    def update_medicine(self, name, quantity):
        if name in self.medicines:
            self.medicines[name] = quantity
            print("Medicine quantity updated successfully.")
        else:
            print("Medicine not found. Please add it first.")

    def view_stock(self):
        print("Current Stock:")
        for name, quantity in self.medicines.items():
            print(f"{name}: {quantity}")

# Main program
pharmacy = PharmacyManagementSystem()

while True:
    print("\nPharmacy Management System")
    print("1. Add Medicine")
    print("2. Update Medicine Quantity")
    print("3. View Stock")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter medicine name: ")
        quantity = int(input("Enter quantity: "))
        pharmacy.add_medicine(name, quantity)
    elif choice == '2':
        name = input("Enter medicine name: ")
        quantity = int(input("Enter new quantity: "))
        pharmacy.update_medicine(name, quantity)
    elif choice == '3':
        pharmacy.view_stock()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
