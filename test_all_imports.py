#!/usr/bin/env python3
"""
Test script to verify all possible import paths that Render might be using.
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

def test_import(name, import_stmt):
    """Test an import statement and report results."""
    print(f"Testing: {import_stmt}")
    try:
        exec(import_stmt)
        print(f"  ✓ SUCCESS")
        return True
    except Exception as e:
        print(f"  ✗ FAILED: {e}")
        return False

def main():
    print("=== TESTING ALL POSSIBLE RENDER IMPORTS ===")
    print(f"Project root: {project_root}")
    print()
    
    # List of import statements that Render might be trying
    imports_to_test = [
        "import app",
        "from app import application",
        "from inventory_management.wsgi import application",
        "import ims",
        "from ims import models",
    ]
    
    results = []
    for import_stmt in imports_to_test:
        success = test_import(import_stmt, import_stmt)
        results.append((import_stmt, success))
        print()
    
    print("=== SUMMARY ===")
    all_success = True
    for import_stmt, success in results:
        status = "✓" if success else "✗"
        print(f"{status} {import_stmt}")
        if not success:
            all_success = False
    
    if all_success:
        print("\n✓ All imports successful!")
    else:
        print("\n✗ Some imports failed. Check the errors above.")

if __name__ == "__main__":
    main()