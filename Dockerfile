FROM python:3

ENV PYTHONBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

RUN apt update
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:ubuntugis/ppa -y
RUN apt-get install gdal-bin -y

COPY . /code/