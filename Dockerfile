# Use a base image with Python and required dependencies
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code
COPY . .

# Expose the Flask app port
EXPOSE 5000

# Set the entry point command
CMD ["python", "app.py"]
