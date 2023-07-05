import pytest
import sys 
import os



from Passenger import Passenger


class Test_Passenger:

    dataMap = {}

    def setup_class(self):
        self.dataMap["PassengerId"] = 1
        self.dataMap["Pclass"] = '3'
        self.dataMap["Name"] = 'John Smith'
        self.dataMap["Sex"] = 'M'
        self.dataMap["Age"] = 20.0
        self.dataMap["SibSp"] = 1
        self.dataMap["Parch"] = 1
        self.dataMap["Ticket"] = 'H732'
        self.dataMap["Fare"] = 7
        self.dataMap["Cabin"] = 'H300'
        self.dataMap["Embarked"] = 'Y'


    def test_PassengerId(self):
        """
        PassengerId = int
        Pclass = str
        Name = str
        Sex = str
        Age = float
        SibSp = int
        Parch = int
        Ticket = str
        Fare = int
        Cabin = str
        Embarked = str
        """



        passenger = Passenger(self.dataMap["PassengerId"],
        self.dataMap["Pclass"],
        self.dataMap["Name"],
        self.dataMap["Sex"],
        self.dataMap["Age"],
        self.dataMap["SibSp"],
        self.dataMap["Parch"],
        self.dataMap["Ticket"],
        self.dataMap["Fare"],
        self.dataMap["Cabin"],
        self.dataMap["Embarked"])

        assert passenger.get_PassengerId() == 1

    def test_Pclass(self):
        """
        PassengerId = int
        Pclass = str
        Name = str
        Sex = str
        Age = float
        SibSp = int
        Parch = int
        Ticket = str
        Fare = int
        Cabin = str
        Embarked = str
        """
        passenger = Passenger(self.dataMap["PassengerId"],
        self.dataMap["Pclass"],
        self.dataMap["Name"],
        self.dataMap["Sex"],
        self.dataMap["Age"],
        self.dataMap["SibSp"],
        self.dataMap["Parch"],
        self.dataMap["Ticket"],
        self.dataMap["Fare"],
        self.dataMap["Cabin"],
        self.dataMap["Embarked"])
        assert passenger.get_Pclass() == '3'
     
    def test_Name(self):
        """
        PassengerId = int
        Pclass = str
        Name = str
        Sex = str
        Age = float
        SibSp = int
        Parch = int
        Ticket = str
        Fare = int
        Cabin = str
        Embarked = str
        """
        passenger = Passenger(self.dataMap["PassengerId"],
        self.dataMap["Pclass"],
        self.dataMap["Name"],
        self.dataMap["Sex"],
        self.dataMap["Age"],
        self.dataMap["SibSp"],
        self.dataMap["Parch"],
        self.dataMap["Ticket"],
        self.dataMap["Fare"],
        self.dataMap["Cabin"],
        self.dataMap["Embarked"])
        assert passenger.get_Name() == 'John Smith'

    def test_Sex(self):
        """
        PassengerId = int
        Pclass = str
        Name = str
        Sex = str
        Age = float
        SibSp = int
        Parch = int
        Ticket = str
        Fare = int
        Cabin = str
        Embarked = str
        """
        passenger = Passenger(self.dataMap["PassengerId"],
        self.dataMap["Pclass"],
        self.dataMap["Name"],
        self.dataMap["Sex"],
        self.dataMap["Age"],
        self.dataMap["SibSp"],
        self.dataMap["Parch"],
        self.dataMap["Ticket"],
        self.dataMap["Fare"],
        self.dataMap["Cabin"],
        self.dataMap["Embarked"])
        assert passenger.get_Sex() == 'M'
        assert type(passenger.get_Sex()) == str