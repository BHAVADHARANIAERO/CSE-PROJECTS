# A list to store patient records (each patient is a dictionary)
patients = []

def add_patient():
    """Adds a new patient record to the system."""
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Patient Age: ")
    gender = input("Enter Patient Gender: ")
    diagnosis = input("Enter Patient Diagnosis: ")

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "diagnosis": diagnosis
    }
    patients.append(patient)
    print(f"Patient {name} added successfully.")

def view_patients():
    """Displays all patient records."""
    if not patients:
        print("No patients in the system.")
        return

    print("\n--- All Patients ---")
    for patient in patients:
        print(f"ID: {patient['id']}, Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, Diagnosis: {patient['diagnosis']}")
    print("--------------------")

def search_patient():
    """Searches for a patient by ID."""
    search_id = input("Enter Patient ID to search: ")
    found = False
    for patient in patients:
        if patient['id'] == search_id:
            print("\n--- Patient Found ---")
            print(f"ID: {patient['id']}, Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, Diagnosis: {patient['diagnosis']}")
            print("---------------------")
            found = True
            break
    if not found:
        print(f"Patient with ID {search_id} not found.")

def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add New Patient")
        print("2. View All Patients")
        print("3. Search Patient by ID")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            search_patient()
        elif choice == '4':
            print("Exiting Hospital Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
