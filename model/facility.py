# models/facility.py
from model.record import Record

class Facility(Record):
    def __init__(self, region, district, license_number, facility_name, facility_type,
                 facility_address_1, facility_address_2, facility_address_3, 
                 max_children, max_infants, max_preschool, max_school_age, 
                 language_of_service, operator_id, designated_facility):
        super().__init__(license_number, facility_name)
        self.region = region
        self.district = district
        self.facility_type = facility_type
        self.facility_address_1 = facility_address_1
        self.facility_address_2 = facility_address_2
        self.facility_address_3 = facility_address_3
        self.max_children = max_children
        self.max_infants = max_infants
        self.max_preschool = max_preschool
        self.max_school_age = max_school_age
        self.language_of_service = language_of_service
        self.operator_id = operator_id
        self.designated_facility = designated_facility

    def display(self):
        return f"Facility Name: {self.name}, License Number: {self.license_number}, Region: {self.region}"

