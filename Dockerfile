FROM resin/rpi-raspbian:wheezy

ENV INITSYSTEM on

RUN apt-get update

RUN apt-get upgrade -y

RUN apt-get install -y python wget build-essential python-dev python-pip

RUN pip install RPi.Gpio

RUN pip install pyowm

ADD gpio_example.py /App/

CMD ["python", "/App/gpio_example.py"]