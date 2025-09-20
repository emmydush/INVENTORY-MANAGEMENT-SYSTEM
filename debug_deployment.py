#!/usr/bin/env python3
"""
Debug script for deployment issues.
This script can be used to diagnose import problems during deployment.
"""

import sys
import os
from pathlib import Path

def debug_deployment():
    """Debug deployment environment and imports."""
    print("=== DEPLOYMENT DEBUG INFO ===")
    
    # Print environment information
    print(f"Current working directory: {os.getcwd()}")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}")
    
    # Print environment variables
    print("\n=== ENVIRONMENT VARIABLES ===")
    env_vars = [
        'DJANGO_SETTINGS_MODULE',
        'PYTHONPATH',
        'PATH',
    ]
    for var in env_vars:
        value = os.environ.get(var, '<not set>')
        print(f"{var}: {value}")
    
    # Print Python path
    print("\n=== PYTHON PATH ===")
    for i, path in enumerate(sys.path):
        print(f"{i}: {path}")
    
    # Check project structure
    project_dir = Path(__file__).resolve().parent
    print(f"\n=== PROJECT STRUCTURE ===")
    print(f"Project directory: {project_dir}")
    
    # Check for key files/directories
    key_paths = [
        'app.py',
        'inventory_management',
        'inventory_management/__init__.py',
        'inventory_management/wsgi.py',
        'ims',
        'manage.py',
    ]
    
    for path in key_paths:
        full_path = project_dir / Path(path)
        exists = full_path.exists()
        is_dir = full_path.is_dir() if exists else False
        print(f"{path}: {'EXISTS' if exists else 'MISSING'}" + (f" (DIR)" if is_dir and exists else "" if exists else ""))
    
    # Test imports
    print("\n=== IMPORT TESTS ===")
    
    import_tests = [
        ("import app", "import app"),
        ("from app import application", "from app import application"),
        ("from app import app", "from app import app"),
        ("import inventory_management", "import inventory_management"),
        ("from inventory_management import wsgi", "from inventory_management import wsgi"),
        ("from inventory_management.wsgi import application", "from inventory_management.wsgi import application"),
    ]
    
    for description, import_stmt in import_tests:
        try:
            exec(import_stmt)
            print(f"✓ {description}")
        except Exception as e:
            print(f"✗ {description} - {e}")
    
    print("\n=== DEBUG COMPLETE ===")

if __name__ == "__main__":
    debug_deployment()