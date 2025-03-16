# persistence/file_io.py
# Importing necessary libraries
import csv
import uuid
from typing import List
from model.facility import Facility

# Function to read facility records from a CSV file
def read_facility_records(file_path: str) -> List[Facility]:
    facilities = []  # List to store the Facility objects
    try:
        # Open the file in read mode
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)  # Create a CSV reader object
            next(csv_reader)  # Skip the header row
            for i, row in enumerate(csv_reader):
                # Check if the row has exactly 15 columns
                if len(row) == 15:
                    # Unpack row data and create a Facility object
                    facility = Facility(*row)  
                    facilities.append(facility)  # Append the facility to the list
                if i == 99:  # Stop reading after 100 records
                    break
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")  # Handle file not found error
    return facilities  # Return the list of facility objects

# Function to write facility records to a CSV file
def write_facility_records(file_path: str, records: List[Facility]) -> None:
    try:
        # Open the file in write mode, with newline='' to prevent blank rows in CSV
        with open(file_path, mode='w', newline='') as file:
            csv_writer = csv.writer(file)  # Create a CSV writer object
            # Write the header row
            csv_writer.writerow(['Region', 'District', 'License-Number', 'Facility-Name', 'Facility-Type', 
                                 'Facility-Address-1', 'Facility-Address-2', 'Facility-Address-3', 
                                 'Max-Number-of-Children', 'Max-Number-of-Infants', 'Max-Number-of-Preschool-Aged-Children',
                                 'Max-Number-of-School-Age-Children', 'Language-of-Service', 'Operator-Id', 'Designated-Facility'])
            # Iterate over the records and write each record as a row in the CSV file
            for record in records:
                csv_writer.writerow([record.region, record.district, record.license_number, record.facility_name, 
                                     record.facility_type, record.facility_address_1, record.facility_address_2, 
                                     record.facility_address_3, record.max_children, record.max_infants, 
                                     record.max_preschool, record.max_school_age, record.language_of_service, 
                                     record.operator_id, record.designated_facility])
    except Exception as e:
        print(f"Error: Unable to write to file: {e}")  # Handle other potential errors

# Function to generate a unique filename using UUID
def generate_uuid_filename() -> str:
    # Generate and return a unique filename with .csv extension
    return str(uuid.uuid4()) + ".csv"
