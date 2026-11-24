FROM python:3.10-slim

WORKDIR /app
COPY prepare_dataframe/requirements.txt .
RUN pip install -r requirements.txt

ENV DATA_DIR=$(DATA_DIR)

COPY prepare_dataframe/prepare_dataframe.py .

CMD ["python prepare_dataframe.py"]