
class Passenger():
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



    def __init__(self, PassengerId, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked):
        self.PassengerId = PassengerId
        self.Pclass = Pclass
        self.Name = Name
        self.Sex = Sex
        self.Age = Age
        self.SibSp = SibSp
        self.Parch = Parch
        self.Ticket = Ticket
        self.Fare = Fare
        self.Cabin = Cabin
        self.Embarked = Embarked

    def get_PassengerId(self):
        return self.PassengerId

    def get_Pclass(self):
        return self.Pclass
    
    def get_Name(self):
        return self.Name

    def get_Sex(self):
        return self.Sex
    def get_Age(self):
        return self.Age
    def get_Sibsp(self):
        return self.SibSp 
    def get_Parch(self):
        return self.Parch
    def get_Ticket(self):
        return self.Ticket
    def get_Fare(self):
        return self.Fare
    def get_Cabin(self):
        return self.Cabin
    def get_Embarked(self):
        return self.Embarked

    
    




