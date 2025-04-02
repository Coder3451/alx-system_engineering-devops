From ubuntu:16.04

RUN apt-get update && apt-get install -y apache2

COPY ./index.html /var/www/html/

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
