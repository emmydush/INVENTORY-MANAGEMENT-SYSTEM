@echo off
echo === BUILD SCRIPT START ===
echo Current directory: %CD%
echo Python path: %PYTHONPATH%
echo.

echo === CHECKING DIRECTORY STRUCTURE ===
dir
echo.

echo === CHECKING APP MODULE ===
if exist app.py (
    echo app.py file found
) else (
    echo app.py file NOT found
)
echo.

echo === TESTING PYTHON IMPORTS ===
python -c "import sys; print('Python version:', sys.version)"
python -c "from app import app; print('App module imported successfully')"
python -c "from app import application; print('Application imported successfully')"
echo.

echo === INSTALLING DEPENDENCIES ===
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to install dependencies
    exit /b %ERRORLEVEL%
)
echo.

echo === COLLECTING STATIC FILES ===
python manage.py collectstatic --noinput
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to collect static files
    exit /b %ERRORLEVEL%
)
echo.

echo === APPLYING MIGRATIONS ===
python manage.py migrate
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to apply migrations
    exit /b %ERRORLEVEL%
)
echo.

echo === BUILD SCRIPT END ===
echo Build completed successfully!