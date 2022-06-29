FROM python:3.8

RUN apt-get install -y python3-dev
RUN apt-get install -y python3-dev

WORKDIR /app

ADD ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

ADD . .

CMD [ "python", "main.py" ]
