FROM python:3.9

WORKDIR /opt/hello_world

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["python", "hello_world.py"]
