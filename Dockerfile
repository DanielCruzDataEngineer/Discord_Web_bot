FROM python:3.7.9-slim

ARG DISCORD_TOKEN
ENV DISCORD_TOKEN=$DISCORD_TOKEN


COPY requirements.txt app/requirements.txt

#install all requirements in requirements.txt
RUN pip install -r app/requirements.txt

#Copy all files in current directory into app directory
COPY . /web_app_v3

#Change Working Directory to app directory
WORKDIR /web_app_v3



CMD [ "python3", "v1/" ]