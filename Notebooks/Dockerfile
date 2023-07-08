FROM jupyter/minimal-notebook

WORKDIR /home/joyvan/work/

RUN mkdir -p /home/joyvan/work/Data
COPY /Data/ /home/joyvan/work/Data/


RUN mkdir -p /home/joyvan/work/Notebooks
COPY /Notebooks/ /home/joyvan/work/Notebooks/

WORKDIR /home/joyvan/work/Notebooks/
RUN pip3 install -r requirements.txt

COPY --chown=$user:group hostfolder/* /home/$NB_USER/work/

