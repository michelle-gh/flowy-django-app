FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR .
ADD requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/
COPY ./flowersproject /app/
WORKDIR /app/
EXPOSE 8000
RUN addgroup --gid 1000 user
RUN adduser --disabled-password --gecos '' --uid 1000 --gid 1000 user
USER user
CMD python manage.py runserver 0.0.0.0:8000