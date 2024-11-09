# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements file if you have one (optional)
# COPY requirements.txt .

# Install FastAPI and Uvicorn (and any other dependencies if needed)
RUN pip install fastapi uvicorn

# Copy the FastAPI app to the container
COPY . .

# Expose the default FastAPI port
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
