# Use the official Python image from the Docker Hub
FROM python:3.9.19

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python-dev \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the specified port
EXPOSE $PORT

# Specify the command to run the Streamlit app
CMD ["streamlit", "run", "gen_app.py", "--server.port=$PORT", "--server.address=0.0.0.0"]
