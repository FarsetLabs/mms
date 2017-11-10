.PHONY:		devserver migrations migrate test clean

behave:
	cd src; python manage.py behave --settings mms.settings.test 

clean:
	find . -name "*pyc" -exec rm -f {} \;

devserver: clean
	cd src; python manage.py runserver 0.0.0.0:8000

migrate:
	cd src; python manage.py migrate

migrations:
	cd src; python manage.py makemigrations

test:
	cd src; python manage.py test -v2

