FROM ubuntu:22.04

RUN apt update && apt install -y python3 python3-pip

WORKDIR /myportfolio

COPY . .

RUN pip3 install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
