### Intro ###


This is a project focused on creating stnadrad process and procedures in working on a machine learning model in a source control system. The data or this project is the Titanic dataset due to the avaiability of different modeling techniques and coverage of the use case. 

The project is broken up into seperate compenents 

1. Application Programming Interface
2. Notebooks
3. IAC
4. Data
5. Train



### Application Programming Interface (API) ###

The API is built as a webservice to be hosted using the flask framework. 

The process for building the API container is the foollowing docker commands. 

docker build -t titanic . 

docker container in -it titanic



$ python app.py




PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked


### Notebooks ###

ro buidl docker image

docker build -t titanic/eda -f Notebooks/DockerFile . 


to run Notebooks 


docker container run -p 8888:8888 titanic/eda