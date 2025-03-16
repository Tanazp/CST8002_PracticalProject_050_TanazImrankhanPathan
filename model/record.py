# models/record.py
from abc import ABC, abstractmethod

class Record(ABC):
    def __init__(self, license_number, name):
        self.license_number = license_number
        self.name = name

    @abstractmethod
    def display(self):
        pass
