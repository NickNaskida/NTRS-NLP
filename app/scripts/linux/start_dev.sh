export FLASK_APP=manage
export FLASK_ENV=development
export FLASK_DEBUG=1

pip install -r requirements.txt

flask db init
flask db migrate
flask db upgrade

flask run