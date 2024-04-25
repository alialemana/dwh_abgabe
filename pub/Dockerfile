FROM python:3.8

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1 

CMD ["python", "-u", "/app/publisher.py"]
