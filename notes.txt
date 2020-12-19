# iParty

## install:
python -m venv env

ctrl+shift+'

pip install flask

python -m pip install --upgrade pip

pip install flask-restful
pip install flask-jwt-auth

pip install pymongo
pip install pymongo[srv]

## create dependecies file
pip freeze > requirements.txt

## Heroku
instalar o heroku 

heroku apps:create cs50-final-project-flask
heroku login
heroku buildpacks:clear -a cs50-final-project-flask
heroku ps:scale web=1 -a cs50-final-project-flask

heroku logs --tail -a cs50-final-project-flask

https://cs50-final-project-flask.herokuapp.com/