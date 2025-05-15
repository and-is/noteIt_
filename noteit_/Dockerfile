# Python image as base
FROM python:3.13-slim

# Set working directory inside the container
WORKDIR /app

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY ./app ./app
COPY .env .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
