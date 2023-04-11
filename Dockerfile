FROM python:latest

COPY src /src
COPY run.sh /run.sh
COPY requirements.txt /requirements.txt

EXPOSE 5000

CMD [ "bash","/run.sh" ]