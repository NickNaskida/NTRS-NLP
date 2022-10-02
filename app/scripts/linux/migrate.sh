export FLASK_APP=manage
flask db migrate
flask db upgrade