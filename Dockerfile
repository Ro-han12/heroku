# Use the official Python image from the Docker Hub
FROM python:3.9.19

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the specified port
EXPOSE $PORT

# Specify the command to run the app using Gunicorn
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:$PORT", "main:gen_app"]
