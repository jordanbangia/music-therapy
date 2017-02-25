# music-therapy
Alzheimer Music Therapy Website for Alzheimers Society of Peel

Built with Hamza Sami and Ali El Hamouly.

This website implements a series of forms for online tracking of Alzheimer's clients goals, assessments, and provides views of their progress.

The site is hosted on Heroku, after making any kind of database changes, they need to be updated on Heroku.  That can be done by running:

    heroku run python manage.py migrate --app App

You can also re add the initial domain/goal data by running:

    heroku run python musictherapy/initial_data.py --app App

