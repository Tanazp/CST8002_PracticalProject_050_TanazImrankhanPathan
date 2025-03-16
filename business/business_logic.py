from typing import List
from model.facility import Facility

def add_facility(facilities: List[Facility], facility: Facility) -> List[Facility]:
    facilities.append(facility)
    return facilities

def edit_facility(facilities: List[Facility], license_number: str, updated_facility: Facility) -> List[Facility]:
    for i, facility in enumerate(facilities):
        if facility.license_number == license_number:
            facilities[i] = updated_facility  # Update the record
            return facilities
    print(f"Facility with License Number {license_number} not found.")
    return facilities

def delete_facility(facilities: List[Facility], license_number: str) -> List[Facility]:
    facilities = [facility for facility in facilities if facility.license_number != license_number]
    return facilities

def view_facilities(facilities: List[Facility], license_number: str = None):
    if license_number:
        for facility in facilities:
            if facility.license_number == license_number:
                print(facility)
                return
        print(f"Facility with License Number {license_number} not found.")
    else:
        for facility in facilities:
            print(facility)
