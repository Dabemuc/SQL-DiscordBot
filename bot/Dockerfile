FROM python:3.8-slim-buster

# Create the bot's directory
RUN mkdir -p /usr/src/bot

COPY bot.py /usr/src/bot

RUN apt update
#RUN apt install python3 -y


RUN python3 -m pip install -U discord.py
RUN python3 -m pip install mariadb
RUN python3 /usr/src/bot/bot.py