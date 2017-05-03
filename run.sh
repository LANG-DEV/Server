pip install -r requirements.txt
python manage.py migrate
python manage.py makemigrations server
python manage.py runserver