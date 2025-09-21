# infra/Dockerfile

# 1. Use slim Python base image for smaller footprint
FROM python:3.12-slim

# 2. Set working directory
WORKDIR /app

# 3. Install system dependencies (needed for some Python libs like lxml, faiss)
RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2 \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy app source code
COPY app/ app/

# 6. Expose port
EXPOSE 8080

# 7. Run the API with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
