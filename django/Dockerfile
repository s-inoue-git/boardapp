FROM python:3.7.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
WORKDIR /code/20201004_BoardApp
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
