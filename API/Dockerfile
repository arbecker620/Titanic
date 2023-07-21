FROM python:3.8-slim-buster

WORKDIR /app

COPY /API/  /app/API/
#ADD titanic /app/

WORKDIR /app/API/
RUN pip3 install -r requirements.txt

#COPY . .
#CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]