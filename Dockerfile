FROM jbarlow83/ocrmypdf

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app

RUN pip install -r requirements.txt

ADD server.py /app

CMD ["hug", "-f", "server.py"]
