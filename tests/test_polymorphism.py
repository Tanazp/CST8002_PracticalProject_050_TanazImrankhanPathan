import unittest  # Importing the unittest module to create and run tests
from model.facility import Facility  # Importing the Facility class from the model.facility module
from model.record import Record  # Importing the Record class from the model.record module (though it's not used in this test)

class TestPolymorphism(unittest.TestCase):  # Define a test case class inheriting from unittest.TestCase
    def test_display_method(self):  # Define the test method for testing polymorphism
        # Creating a Facility object with test data
        facility = Facility("Region1", "District1", "LN001", "Facility1", "Type1", 
                             "Address1", "Address2", "Address3", 100, 10, 20, 30, 
                             "English", "Operator1", "Yes")
        
        # Asserting that the display() method of the Facility object returns the expected string
        self.assertEqual(facility.display(), "Facility Name: Facility1, License Number: LN001, Region: Region1")

# The following block runs the test case when the script is executed directly
if __name__ == "__main__":  
    unittest.main()  # Running the tests
