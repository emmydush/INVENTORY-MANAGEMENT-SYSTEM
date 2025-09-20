#!/usr/bin/env python3
"""
Script to run the Inventory Management System in production mode on Windows.
This uses Django's built-in runserver command with production-like settings.
For true production deployment on Windows, consider using IIS with wfastcgi.
"""

import os
import sys
import subprocess

def run_production_server():
    """Run the Django application in a production-like mode."""
    # Get the directory of this script
    project_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to the project directory
    os.chdir(project_dir)
    
    # Set production environment variable
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_management.settings')
    
    # For production on Windows, we'll use runserver with specific settings
    # Note: This is not a true production server, but suitable for Windows environments
    cmd = [
        'python', 'manage.py', 'runserver', 
        '0.0.0.0:8000',  # Bind to all interfaces
        '--noreload'     # Disable auto-reloader for production-like behavior
    ]
    
    print("Starting Inventory Management System in production mode...")
    print(f"Command: {' '.join(cmd)}")
    print("Server will be available at http://0.0.0.0:8000")
    print("Press Ctrl+C to stop the server")
    print("\nNOTE: For true production deployment on Windows, consider using IIS with wfastcgi.")
    print("For Unix/Linux systems, use Gunicorn as described in GUNICORN.md")
    
    # Run the server
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running server: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        sys.exit(0)

if __name__ == "__main__":
    run_production_server()