FROM python:3.10.12-alpine3.18

# Specify the working directory

WORKDIR /sahihi-text-services

COPY requirements.txt .

# Install build tools
RUN apk add --no-cache build-base linux-headers nginx

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Runs only when the container is running

CMD ["sh", "-c", "python manage.py collectstatic --noinput && python manage.py makemigrations && python manage.py migrate && uwsgi --ini uwsgi.ini"]

