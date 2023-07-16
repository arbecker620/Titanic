FROM jupyter/minimal-notebook

ARG USER_ID=1000
ARG GROUP_ID=1000

WORKDIR /home/joyvan/work/

RUN mkdir -p /home/joyvan/work/Data/
COPY /Data/ /home/joyvan/work/Data/


RUN mkdir -p /home/joyvan/work/Notebooks
COPY /Notebooks/ /home/joyvan/work/Notebooks/

WORKDIR /home/joyvan/work/Notebooks/
RUN pip3 install -r requirements.txt



