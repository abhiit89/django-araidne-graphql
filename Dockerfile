FROM python:3.8.18-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN pip install pipenv
COPY . /app/
RUN pipenv install --dev
EXPOSE 8000