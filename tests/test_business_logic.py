import unittest
from business.business_logic import add_facility, edit_facility, delete_facility, view_facilities
from model.facility import Facility

class TestBusinessLogic(unittest.TestCase):
    def setUp(self):
        self.facility1 = Facility("Region1", "District1", "LN001", "Facility1", "Type1", 
                                  "Address1", "Address2", "Address3", 100, 10, 20, 30, 
                                  "English", "Operator1", "Yes")
        self.facility2 = Facility("Region2", "District2", "LN002", "Facility2", "Type2", 
                                  "Address1", "Address2", "Address3", 50, 5, 10, 15, 
                                  "Spanish", "Operator2", "No")
        self.facilities = [self.facility1, self.facility2]

    def test_add_facility(self):
        new_facility = Facility("Region3", "District3", "LN003", "Facility3", "Type3", 
                                "Address1", "Address2", "Address3", 75, 7, 12, 18, 
                                "French", "Operator3", "Yes")
        updated_facilities = add_facility(self.facilities, new_facility)
        self.assertEqual(len(updated_facilities), 3)

    def test_edit_facility(self):
        updated_facility = Facility("Region1", "District1", "LN001", "Updated Facility1", "Type1", 
                                    "Updated Address1", "Address2", "Address3", 150, 20, 30, 40, 
                                    "English", "Operator1", "Yes")
        updated_facilities = edit_facility(self.facilities, "LN001", updated_facility)
        self.assertEqual(updated_facilities[0].facility_name, "Updated Facility1")

    def test_delete_facility(self):
        updated_facilities = delete_facility(self.facilities, "LN001")
        self.assertEqual(len(updated_facilities), 1)

    def test_view_facilities(self):
        view_facilities(self.facilities)
        # You can add assertions for specific outputs in the test.
