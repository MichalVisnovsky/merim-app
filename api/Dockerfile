FROM python:3.10

WORKDIR /app

RUN mkdir -p /app/log/*

RUN chmod -xrw /app/log/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

EXPOSE 8000

CMD ["python", "-u", "-m", "src.server"]
