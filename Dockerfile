FROM python:3.10-alpine

WORKDIR /world-of-games

COPY ["./WorldOfGames/", "./"]

RUN pip install --no-cache-dir -r requirements.txt

#RUN apk add --no-cache sh

ENV PYTHONPATH /world-of-games

#CMD ["python", "MainGame.py"]