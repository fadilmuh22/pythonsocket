FROM python:slim

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY ./entry.sh /
RUN ["chmod", "+x", "/entry.sh"]

WORKDIR /app
COPY . /app

ENTRYPOINT ["/entry.sh"]
