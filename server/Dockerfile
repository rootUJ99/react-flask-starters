# base image
FROM python:3.7.2-alpine
# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add --no-cache mysql mysql-client && \
    apk add netcat-openbsd
RUN mkdir -p /opt/server
# setting up working directory 
WORKDIR /opt/server
COPY . /opt/server
RUN pip install -r requirements.txt
RUN cat entrypoint.sh
# COPY ./entrypint.sh /opt/server/entrypint.sh
RUN chmod +x /opt/server/entrypoint.sh


# RUN pipenv install --system --deploy
# EXPOSE 5001:5000
CMD ["./entrypoint.sh"]
# CMD ["ls", "-a"]
# CMD python manage.py run -h 0.0.0.0