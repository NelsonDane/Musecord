# Nelson Dane

# Build from node since python doesn't include pip so we have to install python anyways
FROM node:18-alpine

# Install python and pip
RUN apk update && apk add \
    py3-pip \
&& rm -rf /var/cache/apk/*

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     python3-pip \
# && apt-get clean \
# && rm -rf /var/lib/apt/lists/*

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

