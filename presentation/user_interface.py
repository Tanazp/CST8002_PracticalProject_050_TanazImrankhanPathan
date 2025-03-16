import os
from business.business_logic import add_facility, edit_facility, delete_facility, view_facilities
from persistence.file_io import read_facility_records, write_facility_records, generate_uuid_filename
from model.facility import Facility

class UserInterface:
    def __init__(self):
        self.facilities = []

    def show_menu(self):
        while True:
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

            choice = input("Enter choice: ")
            if choice == '1':
                self.load_data()
            elif choice == '2':
                self.view_all_records()
            elif choice == '3':
                self.view_record_by_license_number()
            elif choice == '4':
                self.add_record()
            elif choice == '5':
                self.edit_record()
            elif choice == '6':
                self.delete_record()
            elif choice == '7':
                self.save_data()
            elif choice == '8':
                print("Exiting program.")
                break
            else:
                print("Invalid choice, please try again.")

    def load_data(self):
        file_path = input("Enter file path to load data: ")
        if os.path.exists(file_path):
            self.facilities = read_facility_records(file_path)
            print(f"Loaded {len(self.facilities)} records.")
        else:
            print(f"Error: File '{file_path}' not found.")
    
    def view_all_records(self):
        if not self.facilities:
            print("No records to display.")
        else:
            for facility in self.facilities:
                print(facility)

    def view_record_by_license_number(self):
        license_number = input("Enter License Number to search: ")
        view_facilities(self.facilities, license_number)

    def add_record(self):
        print("Enter details for the new facility:")
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

        new_facility = Facility(region, district, license_number, facility_name, facility_type,
                                facility_address_1, facility_address_2, facility_address_3,
                                max_children, max_infants, max_preschool, max_school_age,
                                language_of_service, operator_id, designated_facility)
        self.facilities = add_facility(self.facilities, new_facility)
        print("New facility added.")

    def edit_record(self):
        license_number = input("Enter License Number of the facility to edit: ")
        # Find the facility by license number
        facility = next((f for f in self.facilities if f.license_number == license_number), None)

        if facility:
            print(f"Editing facility: {facility.facility_name} ({facility.license_number})")

            # Prompt the user for the updated fields
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

            # Create a new Facility object with updated values
            updated_facility = Facility(region, district, license_number, facility_name, facility_type,
                                        facility_address_1, facility_address_2, facility_address_3,
                                        max_children, max_infants, max_preschool, max_school_age,
                                        language_of_service, operator_id, designated_facility)

            # Replace the old facility with the updated one
            self.facilities[self.facilities.index(facility)] = updated_facility
            print("Facility record updated successfully.")
        else:
            print("Facility not found.")

    def delete_record(self):
        license_number = input("Enter License Number of the facility to delete: ")
        self.facilities = delete_facility(self.facilities, license_number)
        print(f"Facility with License Number {license_number} deleted.")

    def save_data(self):
        file_name = generate_uuid_filename()
        write_facility_records(file_name, self.facilities)
        print(f"Data saved to {file_name}.")
