🏥 Simple Console-Based Hospital Management System (HMS)

🌟 Overview of the Project

This project is a fundamental Command-Line Interface (CLI) application developed in Python for basic patient record management.

The primary goal is to demonstrate core Python programming concepts—specifically the use of lists and dictionaries—to create a functional, structured data management system. It simulates the basic operations of a hospital's patient registry, allowing staff to add new patients, view existing records, and search for individuals.

Note: This is an in-memory system; patient data is lost when the application is closed.

✨ Features

The system offers a guided, interactive experience through the following features:

Add New Patient (Creation): Prompts the user for all necessary patient details (ID, Name, Age, Gender, Diagnosis) and successfully stores the record.

View All Patients (Reading): Displays a comprehensive, structured list of every patient record currently held in the system's memory.

Search Patient by ID (Retrieval): Allows users to quickly search for and retrieve a single patient's complete record by inputting their unique ID.

Interactive Menu: A user-friendly loop that continually presents the available options until the user explicitly chooses to exit.

⚙️ Technologies/Tools Used

Tool/Technology

Description

Language

Python 3+

Data Structure

List

Data Structure

Dictionary

Interface

Command Line Interface (CLI)

🚀 Steps to Install & Run the Project

Since this project is a single Python file with no external dependencies, installation is straightforward.

1. Get the Code

You can clone the repository or simply copy the code into a file named hms.py.

2. Run the Application

Open your terminal or command prompt.

Navigate to the directory where you saved the hms.py file.

Execute the script using the Python interpreter:

python hms.py


The main menu will immediately appear in your terminal, and the system will be ready for use.

🧪 Instructions for Testing

To ensure all functions work correctly, follow these steps in order when running the application:

Test 1: Adding a New Patient

From the main menu, enter 1 to Add New Patient.

Input details for a test patient (e.g., ID: P101, Name: Alice, Age: 30, Gender: F, Diagnosis: Flu).

You should see the confirmation message: Patient Alice added successfully.

Test 2: Viewing All Patients

From the main menu, enter 2 to View All Patients.

Verify that the patient you added in Test 1 (P101, Alice) is displayed correctly.

If you have not added any patients, the system should correctly display: No patients in the system.

Test 3: Searching for a Patient

From the main menu, enter 3 to Search Patient by ID.

Successful Search: Enter the ID of the patient you added (P101).

The system should print the complete record for Alice.

Unsuccessful Search (Error Handling): Enter an ID that does not exist (e.g., P999).

The system should print: Patient with ID P999 not found.

Test 4: Exiting the System

From the main menu, enter 4 to Exit.

The program should terminate with the message: Exiting Hospital Management System. Goodbye!
