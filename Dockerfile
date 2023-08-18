FROM python:3.10.12-alpine3.18

# Specify the working directory

WORKDIR /sahihi-text-services

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Runs only when the container is running

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]