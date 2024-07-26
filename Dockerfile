FROM ubuntu:20.04

RUN apt update && apt install -y python3 python3-pip

WORKDIR /myportfolio

COPY . .

RUN python3 install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
