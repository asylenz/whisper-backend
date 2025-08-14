# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for the application
# - unzip is needed for .docx and .pptx file extraction
# - build-essential is good practice for python packages that might need to compile C extensions
RUN apt-get update && apt-get install -y unzip build-essential && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5001

# Define the command to run the application using a production-ready WSGI server
# gunicorn is a popular choice for Flask applications
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
