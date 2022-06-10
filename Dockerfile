# Nelson Dane

# Build from node since python doesn't include pip so we have to install python anyways
FROM node:18

# Env variables
ENV DISCORD_TOKEN = ''

# Install python and pip
RUN apt-get update && apt-get install -y \
    python3-pip \
&& rm -rf /var/lib/apt/lists/*

# Grab needed files
WORKDIR /app
ADD ./musecord.py .
ADD ./LibreScore.sh .
ADD ./requirements.txt .

# Make directories
RUN mkdir ./downloads/

# Install dependencies
RUN pip install -r requirements.txt

CMD ["python3","musecord.py"]

