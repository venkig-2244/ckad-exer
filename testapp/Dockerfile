FROM ubuntu
MAINTAINER itsvenkatesh@gmail.com

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install flask

WORKDIR /app
COPY app.py /app/app.py

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]
