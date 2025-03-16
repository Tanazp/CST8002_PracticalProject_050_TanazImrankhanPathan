# models/facility.py
# Importing the parent class 'Record' from the model.record module
from model.record import Record

# Facility class inherits from the Record class, which contains common properties like 'license_number' and 'facility_name'
class Facility(Record):
    # Constructor to initialize all the attributes for the Facility object
    def __init__(self, region, district, license_number, facility_name, facility_type,
                 facility_address_1, facility_address_2, facility_address_3, 
                 max_children, max_infants, max_preschool, max_school_age, 
                 language_of_service, operator_id, designated_facility):
        
        # Calling the constructor of the parent class 'Record' to initialize common properties
        super().__init__(license_number, facility_name)
        
        # Initializing additional properties specific to Facility
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

    # A method to display the facility details in a formatted way
    def display(self):
        # Returning a string representation of the Facility with key details: name, license number, and region
        return f"Facility Name: {self.name}, License Number: {self.license_number}, Region: {self.region}"
