## Deployment
To deploy the website, first install Python2.7, virtualenv, and pip.

First clone this repo:

    git clone https://github.com/jordanbang/music-therapy.git

Change into the directory, create a virtualenv, activate the environt, and install all the requirements.

    cd music-therapy
    virtualenv venv --no-site-packages
    source venv/bin/activate
    pip install -r requirements.txt

Information on deploying to the site can be found [here](https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/).  Options for deployment include:
- mod_wsgi and Apache, for if you have an existing Apache server
- gunicorn for pure Python WSGI server in UNIX, with no dependencies and easy installation
- uWSGI for fast, developer/sysadmin friendly application container

### Database
A database is required to house all the data.  Any kind of sql database can be used.  It simply needs to be configured in hellodjango/settings.py.  If you have one available, I would recommend using that, otherwise, mysql or sqlite both offer good database systems that will run on both Windows and UNIX machines.


### Key things Before deployment
- Update the secret key (consider using an environment variable) in hellodjango/settings.py

        import os
        SECRET_KEY = os.environ['SECRET_KEY']

 or from a file

        with open('/etc/secret_key.txt') as f:
            SECRET_KEY = f.read().strip()
- turn DEBUG mode off in hellodjango/settings.py
- ALLOWED_HOSTS must be set to a suitable value, should return a static page for incorrect hosts.
- set the database connection parameters
- define STATIC_ROOT and STATIC_URL for the location to serve static files from.
- enable HTTPS so that passwords aren't passed in the clear (only really necessary if the site will be exposed externally)
- LOGGING if logs are desired (incase of errors)

Most of the information on these items can be found [here](https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/).
