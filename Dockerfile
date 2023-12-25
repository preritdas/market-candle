# Use an official Python runtime as a parent image
FROM python:3.12.1-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy just requirements to build dependencies 
COPY requirements.txt .

# Install the dependencies
RUN pip install -U pip wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Add a run script to the PATH
RUN echo 'gunicorn -b :8000 --timeout 0 -k uvicorn.workers.UvicornWorker api:app' > /bin/serve-api && \
    chmod +x /bin/serve-api

# Run the API
CMD exec gunicorn --bind :$PORT --timeout 0 --worker-class uvicorn.workers.UvicornWorker api:app
