FROM python:3.13.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTONUNBUFFERED=1

WORKDIR /code

COPY requirement.txt /code/
RUN pip install -r requirement.txt

COPY . /code/
