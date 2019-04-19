FROM python:3.7.3

RUN apt-get update \
    && apt-get install -y --no-install-recommends

WORKDIR /app/imdbApp
COPY requirements.txt /app/imdbApp
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]