@echo off
echo Starting Inventory Management System with Gunicorn...
echo Server will be available at http://0.0.0.0:8000
echo Press Ctrl+C to stop the server
echo.

gunicorn --bind 0.0.0.0:8000 --workers 3 --timeout 120 --keep-alive 2 inventory_management.wsgi:application