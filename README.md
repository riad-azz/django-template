# DJANGO STARTER TEMPLATE

The Django Starter Template is a minimalistic and ready-to-use template for quickly bootstrapping your Django projects.
It provides a solid foundation and best practices to kickstart your development process.

## Features

This is a simple Django template that provides the following features:

- Folder structure for organizing your Django project.
- Configuration settings for different environments (development, staging, and production).
- Best practices to help you maintain a well-structured Django project.
- Separation of settings into environment-specific files.
- Use of virtual environments for dependency isolation.
- Secure handling of sensitive information using environment variables or configuration files.
- Documentation of code through comments, docstrings, and README files.
- Adherence to Django best practices and conventions.

## Django Settings

To change the database and other settings for the staging and production environments based on this template, you can
follow these steps:

1. Locate the `backend/settings/stage.py` and `backend/settings/prod.py` files within your project structure.
2. Open the stage.py file to modify the staging environment settings and the prod.py file to modify the production
   environment settings.
3. Look for the database configuration section in each file. It typically appears as a dictionary named DATABASES.
4. Adjust the values within the DATABASES dictionary to match your staging and production database settings. Update the
   keys such as `NAME`, `USER`, `PASSWORD`, `HOST`, and `PORT` with the appropriate values for your specific
   environment.
5. If you're using a different database engine (e.g., MySQL), ensure that you update the `ENGINE` key accordingly.
6. Additionally, review other settings such as `SECRET_KEY`, `ALLOWED_HOSTS`, and any other environment-specific
   configurations that may be required for your project.
7. Save the changes in the respective files.

By modifying the stage.py and prod.py files in the `backend/settings/` directory, you can tailor the database and
other settings to match your staging and production environments. Ensure that you use the appropriate values and
configurations for each environment to ensure the smooth operation of your Django project in different deployment
scenarios.