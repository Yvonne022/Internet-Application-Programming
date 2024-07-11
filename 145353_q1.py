# 12345_q1.py
def add_patient(patients, name, age, illness):
    patients.append({'name': name, 'age': age, 'illness': illness})

def display_patients(patients):
    for patient in patients:
        print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")

def search_patient(patients, name):
    for patient in patients:
        if patient['name'] == name:
            print(f"Found patient: Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
            return
    print(f"Patient named {name} not found.")

def remove_patient(patients, name):
    for patient in patients:
        if patient['name'] == name:
            patients.remove(patient)
            print(f"Patient named {name} removed.")
            return
    print(f"Patient named {name} not found.")

def main():
    patients = []
    while True:
        print("\nMenu:")
        print("1. Add Patient")
        print("2. Display All Patients")
        print("3. Search Patient by Name")
        print("4. Remove Patient by Name")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            name = input("Enter patient's name: ")
            age = int(input("Enter patient's age: "))
            illness = input("Enter patient's illness: ")
            add_patient(patients, name, age, illness)
        elif choice == 2:
            display_patients(patients)
        elif choice == 3:
            name = input("Enter patient's name to search: ")
            search_patient(patients, name)
        elif choice == 4:
            name = input("Enter patient's name to remove: ")
            remove_patient(patients, name)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
