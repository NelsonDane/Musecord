# Nelson Dane

# Build from node since python doesn't include pip so we have to install python anyways
FROM node:18-alpine

# Install python, pip, and bash
RUN apk add --no-cache py3-pip bash

# Grab needed files
WORKDIR /app
COPY ./musecord.py .
COPY ./LibreScore.sh .
COPY ./requirements.txt .

# Make directories
RUN mkdir ./downloads/

# Install dependencies
RUN pip install -r requirements.txt

CMD ["python3","musecord.py"]

