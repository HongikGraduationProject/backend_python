FROM python:3.10
WORKDIR /code
COPY requirements.txt .
COPY main.py .
COPY /dto ./dto
COPY /env ./env
COPY /resources ./resources
COPY /utils ./utils
COPY /audios ./audios
RUN pip install -r requirements.txt
CMD ["python","main.py"]