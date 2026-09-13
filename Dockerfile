FROM python:3.12-alpine

WORKDIR /app
COPY app ./app
ENV PORT=8080 APP_VERSION=container
EXPOSE 8080
USER nobody
CMD ["python", "app/main.py"]
