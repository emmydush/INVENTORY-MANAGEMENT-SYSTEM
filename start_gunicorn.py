#!/usr/bin/env python3
"""
Script to run the Inventory Management System with Gunicorn.
This is useful for production deployments.
"""

import os
import sys
import subprocess

def run_gunicorn():
    """Run the Django application using Gunicorn."""
    # Get the directory of this script
    project_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to the project directory
    os.chdir(project_dir)
    
    # Gunicorn command
    cmd = [
        'gunicorn',
        '--bind', '0.0.0.0:8000',
        '--workers', '3',
        '--timeout', '120',
        '--keep-alive', '2',
        'inventory_management.wsgi:application'
    ]
    
    print("Starting Inventory Management System with Gunicorn...")
    print(f"Command: {' '.join(cmd)}")
    print("Server will be available at http://0.0.0.0:8000")
    print("Press Ctrl+C to stop the server")
    
    # Run Gunicorn
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Gunicorn: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        sys.exit(0)

if __name__ == "__main__":
    run_gunicorn()