# Gunakan Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install library
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file project
COPY . .

# Command untuk menjalankan aplikasi
CMD ["python", "app.py"]
