# Use an official lightweight Python image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to be mapped by the ECS service
EXPOSE 5000

# Command to run the application when the container starts
CMD ["python", "app.py"] 