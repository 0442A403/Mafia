FROM python:3.11.0

WORKDIR /app

COPY ../engine/requirements.txt .
RUN pip install -r requirements.txt

COPY ../engine .

ARG single
ENV single=$single
ARG max_player_number
ENV max_player_number=$max_player_number

ENTRYPOINT python . --single=$single --max-player-number=$max_player_number
