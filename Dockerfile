FROM python:3.14.0rc2-alpine3.22

WORKDIR /app

# Install system dependencies
RUN apk update && apk add \
    python3-dev \
    gcc \
    libc-dev \
    git \
    ffmpeg

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Copy project files
COPY . .

# Run the bot
CMD ["python3", "-m", "mbot"]
