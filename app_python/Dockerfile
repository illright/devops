FROM python:3-alpine

RUN mkdir -p /app
RUN mkdir -p /app/data
WORKDIR /app
RUN adduser -D runner && chown -R runner /app

RUN apk add build-base --no-cache

COPY Pipfile Pipfile.lock /app/
RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --system

EXPOSE 3000

USER runner
CMD ["pipenv", "run", "start", "--host=0.0.0.0", "--port=3000"]

COPY main.py /app/
