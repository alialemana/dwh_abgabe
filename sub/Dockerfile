FROM python:3.8

RUN mkdir /app
WORKDIR /app
ADD requirements.txt subscriber.py /app/
RUN pip install -r requirements.txt

CMD ["python","-u", "/app/subscriber.py"]
