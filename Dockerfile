FROM ubuntu:20.04

RUN apt update && apt install -y python3

WORKDIR /myportfolio

COPY . .

RUN pip3 install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
