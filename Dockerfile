FROM python:3.10
WORKDIR /code
COPY requirements.txt .
COPY main.py .
COPY /dto ./dto
COPY /env ./env
COPY /resources ./resources
COPY /utils ./utils
RUN pip install -r requirements.txt
CMD ["python","main.py"]