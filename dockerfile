
FROM python:latest
COPY . .
CMD ["python", "./server.py"]
