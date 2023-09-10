FROM python:3.11.0

WORKDIR /client

COPY ../client/requirements.txt .
RUN pip install -r requirements.txt

COPY ../client .
COPY ../engine/scheme scheme
COPY ../engine/common common

ARG bot_session_id
ENV bot_session_id=$bot_session_id
ARG engine_host
ENV engine_host=$engine_host

ENTRYPOINT python . --bot-session-id=$bot_session_id --engine-host=$engine_host
