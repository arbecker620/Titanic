
docker build -t titanic . 

docker container in -it titanic



$ python app.py




PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked



ro buidl docker image

docker build -t titanic/eda -f Notebooks/DockerFile . 



to run Notebooks 


docker container run -p 8888:8888 titanic/eda