@echo off
echo Using Python version:
python --version

echo Installing dependencies...
pip install -r requirements.txt

echo Collecting static files...
python manage.py collectstatic --noinput

echo Applying database migrations...
python manage.py migrate

echo Build completed successfully!