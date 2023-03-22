FROM tensorflow/tensorflow

RUN apt-get update -y

RUN apt-get install libsndfile1 -y
RUN /usr/bin/python3 -m pip install --upgrade pip
RUN apt-get update && apt-get install -y git

COPY . /app

WORKDIR /app

RUN pip install -r requires.txt

EXPOSE 5000

CMD [ "python", "app2.py" ]

