FROM python:3.8
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
ARG portNumber=8080
ENV PORT=$portNumber
EXPOSE $portNumber
CMD [ "python", "./server.py" ]