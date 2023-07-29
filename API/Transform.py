from Passenger import Passenger

Passenger_Dict = {
    "PassengerId": 1,
    "Pclass": "3",
    "Name": "John Smith",
    "Sex": "M", 
    "Age": 23.0, 
    "SibSp": 1,
    "Parch": 4,
    "Ticket": "O300",
    "Fare": 1.25,
    "Cabin": "L300",
    "Embarked": "S" 
    }


def transform_intake_json(request_dict: dict):





    return names



print(Passenger_Dict.keys())
print(Passenger_Dict.values())

print(Passenger_Dict.get('PassengerId'))

Pass=Passenger(Passenger_Dict.get('PassengerId'),Passenger_Dict.get('Pclass'),Passenger_Dict.get('Name'),Passenger_Dict.get('Sex'),
Passenger_Dict.get('Age'),Passenger_Dict.get('Sibsp'),Passenger_Dict.get('Parch'),Passenger_Dict.get('Ticket'),Passenger_Dict.get('Fare'),Passenger_Dict.get('Cabin'),Passenger_Dict.get('Embarked') )

Passenger_set  = Passenger_Dict.keys()

#P = Passenger()

