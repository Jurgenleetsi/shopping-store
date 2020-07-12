# Base Image
FROM python:3.6

# installing dependencies
RUN pip install django djangorestframework

# create and set working directory
RUN mkdir /app

WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# setting working dir
WORKDIR /app

# Running the
ENTRYPOINT [ "python", "manage.py", "runserver" , "0.0.0.0:8000"]