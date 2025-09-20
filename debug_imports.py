#!/usr/bin/env python3
"""
Debug script to check Python path and module imports in detail.
"""

import sys
import os
from pathlib import Path

def debug_imports():
    print("=== DEBUG IMPORTS ===")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version}")
    
    print("\n=== PYTHON PATH ===")
    for i, path in enumerate(sys.path):
        print(f"{i}: {path}")
    
    print("\n=== CHECKING APP MODULE ===")
    project_root = Path(__file__).resolve().parent
    app_dir = project_root / "app"
    print(f"Project root: {project_root}")
    print(f"App directory exists: {app_dir.exists()}")
    print(f"App directory is dir: {app_dir.is_dir()}")
    
    if app_dir.exists():
        print("App directory contents:")
        for item in app_dir.iterdir():
            print(f"  {item.name} ({'file' if item.is_file() else 'dir'})")
    
    print("\n=== TESTING IMPORTS ===")
    
    # Test 1: Basic sys.path check
    print("1. Checking if app directory is in sys.path...")
    app_in_path = str(app_dir) in sys.path
    print(f"   App directory in sys.path: {app_in_path}")
    
    # Test 2: Direct import test
    print("2. Testing direct import...")
    try:
        import app
        print("   ✓ import app - SUCCESS")
    except Exception as e:
        print(f"   ✗ import app - FAILED: {e}")
    
    # Test 3: WSGI import test
    print("3. Testing WSGI import...")
    try:
        from app.wsgi import application
        print("   ✓ from app.wsgi import application - SUCCESS")
    except Exception as e:
        print(f"   ✗ from app.wsgi import application - FAILED: {e}")
    
    # Test 4: Absolute import test
    print("4. Testing absolute import...")
    try:
        sys.path.insert(0, str(project_root))
        import app as app_abs
        print("   ✓ absolute import app - SUCCESS")
    except Exception as e:
        print(f"   ✗ absolute import app - FAILED: {e}")
    
    # Test 5: Check if this is the issue - maybe Render expects a different structure
    print("5. Checking for alternative module structures...")
    
    # Check if there's an 'application' module that Render might be looking for
    try:
        import application
        print("   ✓ import application - SUCCESS (this might be what Render is looking for)")
    except ImportError:
        print("   ✗ import application - FAILED (as expected)")

if __name__ == "__main__":
    debug_imports()