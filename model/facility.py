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
        self.region = region  # Region where the facility is located
        self.district = district  # The district of the facility
        self.facility_type = facility_type  # Type of the facility (e.g., daycare, school)
        self.facility_address_1 = facility_address_1  # First line of the facility's address
        self.facility_address_2 = facility_address_2  # Second line of the facility's address
        self.facility_address_3 = facility_address_3  # Third line of the facility's address (optional)
        self.max_children = max_children  # Maximum number of children the facility can accommodate
        self.max_infants = max_infants  # Maximum number of infants the facility can accommodate
        self.max_preschool = max_preschool  # Maximum number of preschool-aged children the facility can accommodate
        self.max_school_age = max_school_age  # Maximum number of school-aged children the facility can accommodate
        self.language_of_service = language_of_service  # The language(s) in which services are offered
        self.operator_id = operator_id  # Unique ID of the operator responsible for the facility
        self.designated_facility = designated_facility  # Whether this facility is a designated facility (Yes/No)

    # A method to display the facility details in a formatted way
    def display(self):
        # Returning a string representation of the Facility with key details: name, license number, and region
        return f"Facility Name: {self.name}, License Number: {self.license_number}, Region: {self.region}"
