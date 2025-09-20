# Deploying with Gunicorn

This document explains how to deploy the Inventory Management System using Gunicorn, a Python WSGI HTTP Server.

## What is Gunicorn?

Gunicorn (Green Unicorn) is a Python WSGI HTTP Server for UNIX systems. It's a popular choice for deploying Django applications in production environments.

## Installation

Gunicorn has been added to the [requirements.txt](file:///E:/Best%20App/requirements.txt) file. If you need to install it separately:

```bash
pip install gunicorn
```

## Running with Gunicorn

### Method 1: Using the Python script
```bash
python start_gunicorn.py
```

### Method 2: Direct command
```bash
gunicorn --bind 0.0.0.0:8000 --workers 3 inventory_management.wsgi:application
```

### Method 3: Using the batch file (Windows)
```bash
start_gunicorn.bat
```

## Configuration Options

- `--bind`: The socket to bind to (host:port)
- `--workers`: The number of worker processes (recommended: 2-4x CPU cores)
- `--timeout`: Workers silent for more than this many seconds are killed and restarted
- `--keep-alive`: The number of seconds to wait for requests on a Keep-Alive connection

## Production Deployment

For production deployment, consider:

1. Using a reverse proxy like Nginx in front of Gunicorn
2. Setting up proper logging
3. Configuring static file serving
4. Using environment variables for configuration
5. Setting up process monitoring

Example production command:
```bash
gunicorn --bind 0.0.0.0:8000 --workers 4 --timeout 120 --keep-alive 2 --max-requests 1000 --max-requests-jitter 100 inventory_management.wsgi:application
```

## Common Issues

1. **Port already in use**: Change the port in the `--bind` option
2. **Permission denied**: Ensure you have permission to bind to the specified port
3. **Module not found**: Make sure your virtual environment is activated and all dependencies are installed