# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy all files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask app port
EXPOSE 5003

# # Set environment variables (can also be passed at runtime)
# ENV FLASK_APP=app.py \
#     FLASK_RUN_HOST=0.0.0.0 \
#     MYSQL_HOST=host.docker.internal \
#     MYSQL_USER=root \
#     MYSQL_PASSWORD=${MYSQL_ROOT_PASSWORD} \
#     MYSQL_DATABASE=dealdeli_data

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5003"]


