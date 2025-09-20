#!/usr/bin/env python3
"""
Test script to simulate the exact deployment import scenario.
This script mimics how Render would import the application.
"""

import sys
import os
from pathlib import Path

def test_deployment_scenario():
    """Test the exact scenario that happens during Render deployment."""
    print("=== TESTING DEPLOYMENT IMPORT SCENARIO ===")
    
    # Change to project directory (like Render does)
    project_dir = Path(__file__).resolve().parent
    os.chdir(project_dir)
    
    print(f"Current working directory: {os.getcwd()}")
    print(f"Project directory: {project_dir}")
    print(f"Contents of project directory: {list(project_dir.iterdir())}")
    
    # Test the exact import that Render uses
    print("\n=== Testing Render Import (gunicorn app:app) ===")
    try:
        from app import app
        print("✓ Successfully imported app:app")
    except Exception as e:
        print(f"✗ Failed to import app:app - {e}")
        return False
    
    # Test the alternative import that Render might use
    print("\n=== Testing Alternative Render Import (gunicorn app:application) ===")
    try:
        from app import application
        print("✓ Successfully imported app:application")
    except Exception as e:
        print(f"✗ Failed to import app:application - {e}")
        return False
    
    # Test direct inventory_management import
    print("\n=== Testing Direct inventory_management Import ===")
    try:
        from inventory_management.wsgi import application as inventory_app
        print("✓ Successfully imported inventory_management.wsgi:application")
    except Exception as e:
        print(f"✗ Failed to import inventory_management.wsgi:application - {e}")
        return False
    
    # Verify they're the same object
    if app is application and app is inventory_app:
        print("✓ All imports reference the same WSGI application object")
    else:
        print("⚠ WARNING: WSGI application objects are different")
        print(f"  app is application: {app is application}")
        print(f"  app is inventory_app: {app is inventory_app}")
        print(f"  application is inventory_app: {application is inventory_app}")
    
    return True

if __name__ == "__main__":
    success = test_deployment_scenario()
    if success:
        print("\n✓ All deployment import tests passed!")
    else:
        print("\n✗ Some deployment import tests failed.")
        sys.exit(1)