# Deploying to Render

This document provides detailed instructions for deploying the Inventory Management System to Render.

## Prerequisites

1. A Render account (https://render.com)
2. A GitHub/GitLab account to host your repository
3. A PostgreSQL database (Render provides free PostgreSQL databases)

## Deployment Files

This project includes the following files to facilitate deployment to Render:

1. [Procfile](file:///E:/Best%20App/Procfile) - Defines the command to run the web application
2. [render.yaml](file:///E:/Best%20App/render.yaml) - Render blueprint for automatic deployment
3. [runtime.txt](file:///E:/Best%20App/runtime.txt) - Specifies the Python version
4. [.render-buildpacks](file:///E:/Best%20App/.render-buildpacks) - Specifies the buildpack to use
5. [build.bat](file:///E:/Best%20App/build.bat) - Build script for Windows environments
6. [app/](file:///E:/Best%20App/app/) - Module created to resolve "ModuleNotFoundError: No module named 'app'" error

## Deployment Steps

### 1. Prepare Your Repository

1. Push your code to a GitHub/GitLab repository
2. Ensure all the deployment files mentioned above are included in your repository

### 2. Create a New Web Service on Render

1. Log in to your Render account
2. Click "New" and select "Web Service"
3. Connect your GitHub/GitLab account and select your repository
4. Configure the service:
   - Name: Choose a name for your service
   - Region: Select your preferred region
   - Branch: Select the branch to deploy (usually main/master)
   - Root Directory: Leave empty if the project is at the root of the repository
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app.wsgi:application --bind 0.0.0.0:$PORT`

### 3. Add Environment Variables

In the Render dashboard, go to your service settings and add the following environment variables:

```
DEBUG=False
DJANGO_SETTINGS_MODULE=inventory_management.settings
SECRET_KEY=your-secret-key-here
DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=your-database-host
DB_PORT=5432
```

### 4. Create a PostgreSQL Database

1. In Render, click "New" and select "PostgreSQL"
2. Choose a name for your database
3. Select your preferred region
4. Choose the free tier if you're just testing
5. Once created, Render will provide the database connection details

### 5. Connect Database to Web Service

1. In your web service settings, go to "Environment"
2. Add the database connection details as environment variables:
   - DB_NAME: The database name from your PostgreSQL instance
   - DB_USER: The database user from your PostgreSQL instance
   - DB_PASSWORD: The database password from your PostgreSQL instance
   - DB_HOST: The database host from your PostgreSQL instance
   - DB_PORT: Usually 5432 for PostgreSQL

### 6. Deploy

1. Click "Create Web Service" or "Save Changes" if you're updating an existing service
2. Render will automatically start the deployment process
3. You can monitor the build logs in the Render dashboard

## Post-Deployment Setup

After deployment, you may need to run some management commands:

### Create a Superuser

You can create a superuser by using the deploy_setup management command:

```bash
# Set environment variables for the superuser
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=your-password

# Run the deployment setup command
python manage.py deploy_setup
```

Alternatively, you can create a superuser manually by running a one-off command in Render:

```bash
python manage.py createsuperuser --noinput
```

### Run Migrations

Migrations are automatically applied during the build process, but if you need to run them manually:

```bash
python manage.py migrate
```

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'app'**
   - This error has been resolved by creating an 'app' module that proxies to the actual application
   - The [app/](file:///E:/Best%20App/app/) directory contains the necessary files to satisfy this requirement

2. **Database Connection Issues**
   - Verify that all database environment variables are correctly set
   - Ensure the database is provisioned and running
   - Check that the database credentials are correct

3. **Static Files Not Loading**
   - Ensure `STATIC_ROOT` is set in your settings.py
   - Run `python manage.py collectstatic` during the build process
   - Configure your web server to serve static files

### Checking Logs

You can check your application logs in the Render dashboard:
1. Go to your web service
2. Click on "Logs" to view real-time logs
3. Check for any error messages or warnings

## Custom Domain

To use a custom domain:
1. In your Render web service, go to "Settings"
2. Scroll down to "Custom Domains"
3. Add your domain
4. Follow the instructions to configure DNS records

## Scaling

Render allows you to scale your application:
1. Go to your web service settings
2. Under "Plan", you can upgrade from the free tier to a paid plan
3. You can also configure auto-scaling based on metrics

## Environment-Specific Settings

The application is configured to work with environment variables for different environments:
- `DEBUG`: Set to `False` in production
- `SECRET_KEY`: Should be a unique, secret key in production
- Database settings: Should use the Render-provided database credentials