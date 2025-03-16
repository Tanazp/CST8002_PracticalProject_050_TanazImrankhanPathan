# test_polymorphism.py
import pytest
from model.facility import Facility  # Adjusted import for the Facility class
from model.record import Record      # Adjusted import for the Record class

# Test for the polymorphic behavior of the display() method
def test_display_method():
    # Creating a Facility object with test data
    facility = Facility("Region1", "District1", "LN001", "Facility1", "Type1", 
                         "Address1", "Address2", "Address3", 100, 10, 20, 30, 
                         "English", "Operator1", "Yes")
    
    # Assert that the display() method of the Facility object returns the expected string
    assert facility.display() == "Facility Name: Facility1, License Number: LN001, Region: Region1"
