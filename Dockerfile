FROM python:3.10.12-alpine3.18

RUN pip install --upgrade pip

# Specify the working directory

WORKDIR /sahihi-text-services

COPY requirements.txt .

# Install build tools
RUN apk add --no-cache build-base linux-headers

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]

