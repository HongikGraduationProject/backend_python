FROM python:3.10-slim AS build

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10-slim

WORKDIR /code

COPY --from=build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY log_config.py .
COPY main.py .
COPY dto ./dto
COPY env ./env
COPY resources ./resources
COPY utils ./utils
COPY audios ./audios

CMD ["python", "main.py"]