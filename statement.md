# 🏥 Project Statement: Simple Hospital Management System

## 🌟 Mission and Purpose

This simple Python script implements a **console-based Hospital Management System (HMS)** designed for basic patient record keeping.

The primary mission is to provide a straightforward, easy-to-understand, and functional foundation for managing core patient data using fundamental Python data structures: **lists** and **dictionaries**.

## ✨ Key Features

The current system provides the following functionalities:

1.  **Add New Patient:** Captures patient details (ID, Name, Age, Gender, Diagnosis) and stores them as a dictionary within the central `patients` list.
2.  **View All Patients:** Displays a formatted list of all patient records currently in the system.
3.  **Search Patient by ID:** Allows a user to quickly retrieve and view a specific patient's record by entering their unique ID.
4.  **Interactive Menu:** A persistent `main_menu()` loop handles user input and directs program flow until the user chooses to exit.

## ⚙️ Technical Foundation

* **Language:** Python
* **Data Structure:** A global **list** (`patients`) is used to store multiple records, where each individual patient record is represented by a **dictionary**.

## 🚀 Future Enhancements (Roadmap)

While the current system is functional, the following features are planned for future development to enhance its utility:

* **Data Persistence:** Implement functionality to save and load patient data to a file (e.g., CSV, JSON) so records are not lost upon program exit.
* **Error Handling:** Add input validation (e.g., ensuring Age is a number, ID is unique) to make the system more robust.
* **Update/Delete Functionality:** Implement options to modify existing patient records or remove them from the system.
* **Search by Name:** Extend the search function to include searching by patient name.
