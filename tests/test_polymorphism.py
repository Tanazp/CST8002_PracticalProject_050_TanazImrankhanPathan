# tests/test_polymorphism.py
import unittest
from models.facility import Facility
from models.record import Record

class TestPolymorphism(unittest.TestCase):
    def test_display_method(self):
        facility = Facility("Region1", "District1", "LN001", "Facility1", "Type1", 
                             "Address1", "Address2", "Address3", 100, 10, 20, 30, 
                             "English", "Operator1", "Yes")
        self.assertEqual(facility.display(), "Facility Name: Facility1, License Number: LN001, Region: Region1")

if __name__ == "__main__":
    unittest.main()
