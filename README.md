# DJANGO STARTER TEMPLATE

The Django Starter Template is a minimalistic and ready-to-use template for quickly bootstrapping your Django projects.
It provides a solid foundation and best practices to kickstart your development process.

## Getting started

1. Cloning the repo:

```bash
git clone https://github.com/riad-azz/django-template.git
```

2. Installing dependencies:

```bash
cd django-template
```

```bash
python -m pip install -r requirements/base.txt
```

3. Starting the development server:

```bash
python manage.py runserver localhost:8000
```

4. Starting the staging server:

```bash
python manage.stage.py runserver localhost:8000
```

5. Starting the production server:

```bash
python manage.prod.py runserver 0.0.0.0:8000
```

Open http://localhost:8000 with your browser to see the result.

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

## Static & Media Files

To ensure correct configuration of static and media files for production in your Django project, follow these simple
steps:

**Collect Static Files**: Run the following command to collect all static files in one location:

```bash
python manage.prod.py collectstatic
```

This command gathers static files from all installed apps and places them in a designated directory.

**Serve Static Files**: Configure your production server to serve static files directly. Set up your web server (e.g.,
   Nginx, Apache) to handle static file serving efficiently. Configure the web server to serve static files from the
   designated directory where you collected the static files. This ensures that static files are served directly by the
   web server, enhancing performance.

**Configure Media Files**: If your application involves user-uploaded files, follow these steps:
   Define a MEDIA_ROOT setting in your production settings file, specifying the directory where user-uploaded media
   files will be stored. Configure your web server to serve media files from the specified MEDIA_ROOT directory.

Ensure the proper permissions are set for the media directory, allowing the web server to read and write files in that
location.

By following these simple steps, you can configure the static and media files correctly for production in your Django
project. Make sure to thoroughly test the configuration in a production-like environment to ensure the proper handling
of static and media files.