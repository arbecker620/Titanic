### Intro ###

This project is focused on creating standard code and procedures in working on a machine learning system in a source control system. The data for this project is from the Titanic dataset, this is due to the avaiability of different modeling techniques and extensive coverage of the use case. The background information and subsequently various notebooks can be found on the following link [Kaggle Titanic](https://www.kaggle.com/c/titanic)


### Requirements ###

The following is  list of software or applicatioons which need to be installed as apart of the project. Python is not installed directly onto the machine you are using but utilized in the docker containers. This is primarily because I use a M1 Macbook Air with 256gb, I want to avoid having as much software installed on the system as much as possible. So I push the install of python into docker so I can use multiple version without dependency issues. 

1. Ide of your choosing
2. Docker
3. Terraform
4. Docker Compose

The project is broken up into seperate compenents 

1. Application Programming Interface (API)
2. Notebooks
3. Infrastructure as Code (IAC)
4. Data
5. Train



### Application Programming Interface (API) ###

The API is built as a webservice to be hosted using the flask framework. The following commands in docker build the APi Container with the requirements located in the API Folder.  

`docker build -t titanic/api -f API/Dockerfile . `

When specific packages are needed for the API, the adjusts can be made under the requirements.txt file in the API folder. 

The following command will start the container in an interactive mode. 

`docker container run -it titanic/api`


The commands to start the flask service are listed below
$ python app.py 



### Test ###
In the API folder, there is a few tests have included 
PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked


### Notebooks ###
The notebooks folder is where the steps invovling explaratory analysis can occur. the commands to start up this component are listed below


To build docker image

`docker build -t titanic/eda -f Notebooks/DockerFile . `


to run Notebooks 


`docker container run -p 8888:8888 titanic/eda `


### Data ###

As of this moment, the data is downloaded locally and maintained by git. This could be alleviated by when the notebook container is built to pull the data from Kaggle directly instead of keeping a local coppy