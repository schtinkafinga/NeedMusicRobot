FROM python:3.11-alpine3.17

WORKDIR /app

# Install system dependencies
RUN apk add --no-cache \
    python3-dev \
    gcc \
    libc-dev \
    git

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Copy project files
COPY . .

# Run the bot
CMD ["python3", "-m", "mbot"]
