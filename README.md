
# nersc-flask-starter

This builds two images.
One image has a Flask app, and uses Gunicorn to run it.
The other runs nginx.
The static assets are in the nginx container.
It would be nice to have the static assets live in the app dir too, is there a way to make this work?
