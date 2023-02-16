#Base Image to use
FROM python:3.7.9-slim

#Expose port 8080
EXPOSE 8501

#Optional - install git to fetch packages directly from github
RUN apt-get update && apt-get install -y git

#Copy Requirements.txt file into app directory
COPY requirements.txt app/requirements.txt

#install all requirements in requirements.txt
RUN pip install -r app/requirements.txt

#Copy all files in current directory into app directory
COPY . /web_app_v3

#Change Working Directory to app directory
WORKDIR /web_app_v3

ENV PORT 8501

# cmd to launch app when container is run
CMD python v1/

