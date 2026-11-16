from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name: str, phone_number: str):
        self._name = name
        self._phone_number = phone_number

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str):
        self._phone_number = phone_number

    @property
    @abstractmethod
    def id(self):
        """Each user type defines its own id."""

    @id.setter
    @abstractmethod
    def id(self, value):
        pass