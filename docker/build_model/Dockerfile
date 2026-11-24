FROM python:3.10-slim

WORKDIR /app
COPY build_model/requirements.txt .
RUN pip install -r requirements.txt

ENV DATA_DIR=$(DATA_DIR)

COPY build_model/build_model.py .

CMD ["python3 app/build_model.py"]