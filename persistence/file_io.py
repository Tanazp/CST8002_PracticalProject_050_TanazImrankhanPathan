import csv
import uuid
from typing import List
from model.facility import Facility

def read_facility_records(file_path: str) -> List[Facility]:
    facilities = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            for i, row in enumerate(csv_reader):
                if len(row) == 15:  # Ensure there are 15 columns
                    facility = Facility(*row)  # Unpack row data into a Facility object
                    facilities.append(facility)
                if i == 99:  # Stop after 100 records
                    break
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return facilities

def write_facility_records(file_path: str, records: List[Facility]) -> None:
    try:
        with open(file_path, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Region', 'District', 'License-Number', 'Facility-Name', 'Facility-Type', 
                                 'Facility-Address-1', 'Facility-Address-2', 'Facility-Address-3', 
                                 'Max-Number-of-Children', 'Max-Number-of-Infants', 'Max-Number-of-Preschool-Aged-Children',
                                 'Max-Number-of-School-Age-Children', 'Language-of-Service', 'Operator-Id', 'Designated-Facility'])
            for record in records:
                csv_writer.writerow([record.region, record.district, record.license_number, record.facility_name, 
                                     record.facility_type, record.facility_address_1, record.facility_address_2, 
                                     record.facility_address_3, record.max_children, record.max_infants, 
                                     record.max_preschool, record.max_school_age, record.language_of_service, 
                                     record.operator_id, record.designated_facility])
    except Exception as e:
        print(f"Error: Unable to write to file: {e}")

def generate_uuid_filename() -> str:
    return str(uuid.uuid4()) + ".csv"
