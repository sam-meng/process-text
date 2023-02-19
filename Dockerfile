FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /server

# Installing Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application dir
COPY .env* ./
COPY app app
COPY data data

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app.main:app"]
