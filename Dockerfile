# Use the official Python image as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the container's working directory
COPY . /app

# Install project requirements
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python script
CMD ["python", "watch_next.py"]
