FROM python:3.8

RUN mkdir /app
WORKDIR /app
ADD . /app/
ENV PYTHONUNBUFFERED=0
RUN pip install -r requirements.txt

CMD ["python", "/app/subscriber.py"]
