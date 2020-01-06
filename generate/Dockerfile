FROM ubuntu
MAINTAINER itsvenkatesh@gmail.com

RUN apt-get update -y
RUN apt-get install python3 -y

COPY app.py /app/app.py
WORKDIR /app

ENTRYPOINT ["python3"]
CMD ["app.py"]
