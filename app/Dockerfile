FROM python:3.12-slim

WORKDIR /srv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY calculator.py app.py ./
EXPOSE 5000
CMD ["python", "app.py"]
