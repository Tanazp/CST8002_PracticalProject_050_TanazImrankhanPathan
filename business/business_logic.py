# business/business_logic.py
# Importing the Facility class from the model.facility module to work with Facility objects
from typing import List
from model.facility import Facility

# Function to display all the records (facilities) by calling their 'display' method
def display_records(records: List[Facility]):
    # Iterate over the list of records (facilities) and display each record's details
    for record in records:
        print(record.display())
        
# Function to add a new facility to the list of facilities
def add_facility(facilities: List[Facility], facility: Facility) -> List[Facility]:
    # Append the new facility to the list
    facilities.append(facility)
    return facilities

# Function to edit an existing facility based on its license number
def edit_facility(facilities: List[Facility], license_number: str, updated_facility: Facility) -> List[Facility]:
    # Iterate over the list of facilities
    for i, facility in enumerate(facilities):
        # Check if the current facility's license number matches the given license number
        if facility.license_number == license_number:
            # If found, update the facility at the current index with the new details
            facilities[i] = updated_facility  
            return facilities
    # If no matching facility is found, print an error message
    print(f"Facility with License Number {license_number} not found.")
    return facilities

# Function to delete a facility based on its license number
def delete_facility(facilities: List[Facility], license_number: str) -> List[Facility]:
    # Filter the list of facilities, excluding the one with the matching license number
    facilities = [facility for facility in facilities if facility.license_number != license_number]
    return facilities

# Function to view facilities (either by license number or all facilities)
def view_facilities(facilities: List[Facility], license_number: str = None):
    # If a license number is provided, search for that specific facility
    if license_number:
        for facility in facilities:
            if facility.license_number == license_number:
                print(facility.display())  # Display the found facility
                return
        # If no matching facility is found, print an error message
        print(f"Facility with License Number {license_number} not found.")
    else:
        # If no license number is provided, display all facilities
        for facility in facilities:
            print(facility.display())
