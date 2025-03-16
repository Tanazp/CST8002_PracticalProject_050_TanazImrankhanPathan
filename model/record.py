# models/record.py
from abc import ABC, abstractmethod
"""
    Abstract base class for different record types.
    Defines the structure for record classes and an abstract display method.
    """
class Record(ABC):
    def __init__(self, license_number, name):
        self.license_number = license_number
        self.name = name

    @abstractmethod
    def display(self):
        pass
