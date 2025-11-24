🏥 Statement of Hospital Management System
This document outlines the core aspects of the Simple Hospital Management System (HMS) Python script.

1. 🎯 Problem Statement
The fundamental problem addressed by this script is the lack of a simple, digital method for basic patient data record-keeping and retrieval. Manually tracking patient information (ID, name, diagnosis) is inefficient, prone to errors, and difficult to search.

This project offers a foundational solution by establishing an in-memory, structured mechanism (using a list of dictionaries) to efficiently store, display, and search core patient details.

2. 🔭 Scope of the Project
The scope of this initial project is narrow and focused on demonstrating core data management principles using fundamental Python structures.

Inclusions (In Scope):
Data Structure: Using a Python list of dictionaries to hold patient records in memory.

Core CRUD Operations (Create, Read, Search):

Adding a new patient record (C).

Viewing all patient records (R).

Searching for a record by ID (S).

User Interface: A simple, text-based command-line menu.

Exclusions (Out of Scope for initial version):
Data Persistence: Saving data to or loading data from a file (e.g., CSV, JSON).

Advanced Features: Functions for updating or deleting existing records.

Error Handling: Robust validation for input types or unique IDs.

3. 👤 Target Users
The primary target users for this script are:

Computer Science Students/Beginners: Individuals learning Python who need a practical, real-world example of using lists, dictionaries, functions, and loops to build a basic application.

Small Clinic Administrators/Staff: Teams needing a quick, non-persistent tool for managing short-term patient lists in a low-resource setting.

Instructors/Trainers: People looking for a clear, concise code example to teach fundamental object representation and data flow concepts in Python.

4. 💡 High-Level Features
The system offers the following key capabilities:

Patient Registration (Add Patient):

Collects essential patient attributes: ID, Name, Age, Gender, and Diagnosis.

Stores each patient's data as a distinct dictionary object.

System Overview (View All Patients):

Provides a full, structured output of every patient record currently held in the system's memory.

Record Lookup (Search Patient by ID):

Enables fast, direct retrieval of a single patient record by matching a unique Patient ID.

Interactive Menu System:

Uses a while loop to present a persistent, easy-to-navigate menu that guides the user through all available actions.
