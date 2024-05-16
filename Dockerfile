FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python3", "main.py"]