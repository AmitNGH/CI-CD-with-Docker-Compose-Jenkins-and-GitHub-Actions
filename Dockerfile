FROM python:3.10-alpine

WORKDIR /world-of-games

COPY ["./WorldOfGames", "./"]

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "MainGame.py"]