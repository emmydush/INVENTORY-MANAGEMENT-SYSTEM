#!/usr/bin/env python3
"""
Test script to verify that the app module WSGI application can be imported correctly.
"""

import os
import sys
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(project_dir))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_management.settings')

def test_imports():
    """Test importing the WSGI applications."""
    print("Testing WSGI application imports...")
    
    try:
        # Test importing from app module (app.py file, not app directory)
        from app import application as app_application
        print("✓ Successfully imported app:application")
    except Exception as e:
        print(f"✗ Failed to import app:application - {e}")
        return False
    
    try:
        # Test importing from inventory_management module
        from inventory_management.wsgi import application as inventory_application
        print("✓ Successfully imported inventory_management.wsgi:application")
    except Exception as e:
        print(f"✗ Failed to import inventory_management.wsgi:application - {e}")
        return False
    
    # Check if they're the same object
    if app_application is inventory_application:
        print("✓ Both imports reference the same WSGI application object")
    else:
        print("✗ WARNING: WSGI application objects are different")
    
    return True

if __name__ == "__main__":
    success = test_imports()
    if success:
        print("\n✓ All tests passed! The app module is correctly configured.")
    else:
        print("\n✗ Some tests failed. Please check the configuration.")
        sys.exit(1)