export FLASK_APP=manage

flask db init
flask db migrate
flask db upgrade