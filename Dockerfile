FROM jbarlow83/ocrmypdf

USER root

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app

RUN . /appenv/bin/activate && pip install -r requirements.txt

ADD server.py index.htm entrypoint.sh /app/
ADD static /app/static/

USER docker

ENTRYPOINT ["/app/entrypoint.sh"]
