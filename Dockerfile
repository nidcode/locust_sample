FROM locustio/locust:latest

WORKDIR /locust
COPY ./locustfile.py .

CMD ["/usr/local/bin/locust"]