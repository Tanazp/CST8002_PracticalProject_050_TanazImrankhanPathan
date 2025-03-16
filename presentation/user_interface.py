# presentation/user_interface.py

# Import necessary modules and functions
import os
from business.business_logic import add_facility, edit_facility, delete_facility, view_facilities, display_records
from persistence.file_io import read_facility_records, write_facility_records, generate_uuid_filename
from model.facility import Facility

# Define the UserInterface class to interact with the user
class UserInterface:
    def __init__(self):
        self.facilities = []  # Initialize an empty list of facilities

    # Method to display the main menu and process user input
    def show_menu(self):
        while True:
            # Display the options available to the user
            print("\n--- Facility Management System ---")
            print("\n Program by Tanaz Pathan")
            print("1. Load data from file")
            print("2. View all records")
            print("3. View record by License Number")
            print("4. Add new record")
            print("5. Edit record")
            print("6. Delete record")
            print("7. Save data to new file")
            print("8. Exit")

            # Take user input for the selected menu option
            choice = input("Enter choice: ")

            # Execute the corresponding action based on the user's choice
            if choice == '1':
                self.load_data()  # Load data from a file
            elif choice == '2':
                self.view_all_records()  # View all facility records
            elif choice == '3':
                self.view_record_by_license_number()  # View a specific record by License Number
            elif choice == '4':
                self.add_record()  # Add a new facility record
            elif choice == '5':
                self.edit_record()  # Edit an existing facility record
            elif choice == '6':
                self.delete_record()  # Delete a facility record
            elif choice == '7':
                self.save_data()  # Save data to a new file
            elif choice == '8':
                print("Exiting program.")  # Exit the program
                break  # Break the loop to exit the program
            else:
                print("Invalid choice, please try again.")  # Handle invalid choices

    # Method to load facility data from a CSV file
    def load_data(self):
        file_path = input("Enter file path to load data: ")  # Ask user for the file path
        if os.path.exists(file_path):  # Check if the file exists
            self.facilities = read_facility_records(file_path)  # Read records from the file
            print(f"Loaded {len(self.facilities)} records.")  # Display how many records were loaded
        else:
            print(f"Error: File '{file_path}' not found.")  # Error if file does not exist
    
    # Method to view all the facility records
    def view_all_records(self):
        if not self.facilities:  # Check if the facilities list is empty
            print("No records to display.")  # Display message if no records are available
        else:
            display_records(self.facilities)  # Call function to display all records

    # Method to view a specific facility record by License Number
    def view_record_by_license_number(self):
        license_number = input("Enter License Number to search: ")  # Ask for the License Number
        view_facilities(self.facilities, license_number)  # Search and display the facility record

    # Method to add a new facility record
    def add_record(self):
        print("Enter details for the new facility:")
        # Prompt the user to input the details of the new facility
        region = input("Region: ")
        district = input("District: ")
        license_number = input("License Number: ")
        facility_name = input("Facility Name: ")
        facility_type = input("Facility Type: ")
        facility_address_1 = input("Facility Address Line 1: ")
        facility_address_2 = input("Facility Address Line 2: ")
        facility_address_3 = input("Facility Address Line 3: ")
        max_children = input("Max Number of Children: ")
        max_infants = input("Max Number of Infants: ")
        max_preschool = input("Max Number of Preschool-Aged Children: ")
        max_school_age = input("Max Number of School-Age Children: ")
        language_of_service = input("Language of Service: ")
        operator_id = input("Operator ID: ")
        designated_facility = input("Designated Facility (Yes/No): ")

        # Create a new Facility object using the provided details
        new_facility = Facility(region, district, license_number, facility_name, facility_type,
                                facility_address_1, facility_address_2, facility_address_3,
                                max_children, max_infants, max_preschool, max_school_age,
                                language_of_service, operator_id, designated_facility)

        # Add the new facility to the facilities list
        self.facilities = add_facility(self.facilities, new_facility)
        print("New facility added.")  # Notify the user

    # Method to edit an existing facility record
    def edit_record(self):
        license_number = input("Enter License Number of the facility to edit: ")  # Ask for the License Number
        # Find the facility object that matches the License Number
        facility = next((f for f in self.facilities if f.license_number == license_number), None)

        if facility:
            # Facility found, prompt the user to update the details
            print(f"Editing facility: {facility.facility_name} ({facility.license_number})")
            # Ask the user to input the updated details, defaulting to current values if left empty
            region = input(f"Enter Region (current: {facility.region}): ") or facility.region
            district = input(f"Enter District (current: {facility.district}): ") or facility.district
            facility_name = input(f"Enter Facility Name (current: {facility.facility_name}): ") or facility.facility_name
            facility_type = input(f"Enter Facility Type (current: {facility.facility_type}): ") or facility.facility_type
            facility_address_1 = input(f"Enter Facility Address 1 (current: {facility.facility_address_1}): ") or facility.facility_address_1
            facility_address_2 = input(f"Enter Facility Address 2 (current: {facility.facility_address_2}): ") or facility.facility_address_2
            facility_address_3 = input(f"Enter Facility Address 3 (current: {facility.facility_address_3}): ") or facility.facility_address_3
            max_children = input(f"Enter Max Number of Children (current: {facility.max_children}): ") or facility.max_children
            max_infants = input(f"Enter Max Number of Infants (current: {facility.max_infants}): ") or facility.max_infants
            max_preschool = input(f"Enter Max Number of Preschool-Aged Children (current: {facility.max_preschool}): ") or facility.max_preschool
            max_school_age = input(f"Enter Max Number of School-Aged Children (current: {facility.max_school_age}): ") or facility.max_school_age
            language_of_service = input(f"Enter Language of Service (current: {facility.language_of_service}): ") or facility.language_of_service
            operator_id = input(f"Enter Operator ID (current: {facility.operator_id}): ") or facility.operator_id
            designated_facility = input(f"Enter Designated Facility (current: {facility.designated_facility}): ") or facility.designated_facility

            # Create a new Facility object with the updated details
            updated_facility = Facility(region, district, license_number, facility_name, facility_type,
                                        facility_address_1, facility_address_2, facility_address_3,
                                        max_children, max_infants, max_preschool, max_school_age,
                                        language_of_service, operator_id, designated_facility)

            # Replace the old facility with the updated one in the list
            self.facilities[self.facilities.index(facility)] = updated_facility
            print("Facility record updated successfully.")  # Notify the user
        else:
            print("Facility not found.")  # Handle case where the facility is not found

    # Method to delete a facility record
    def delete_record(self):
        license_number = input("Enter License Number of the facility to delete: ")  # Ask for the License Number
        # Delete the facility from the list
        self.facilities = delete_facility(self.facilities, license_number)
        print(f"Facility with License Number {license_number} deleted.")  # Notify the user

    # Method to save the facility data to a new file
    def save_data(self):
        file_name = generate_uuid_filename()  # Generate a unique filename using UUID
        # Save the facility records to the generated file
        write_facility_records(file_name, self.facilities)
        print(f"Data saved to {file_name}.")  # Notify the user
