# use python3.8 image as base image
FROM python:3.8
#set the working directory inside the container
WORKDIR /app
#copy the current directory contents to the container /app
COPY . /app
# install allthe needed packages
RUN pip install requirements.txt
#make port 800 available to the world outside tis container
EXPOSE 8000
#Run Django,s development Server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]