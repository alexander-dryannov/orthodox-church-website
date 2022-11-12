run:
	python manage.py runserver --settings=church_website.settings.pro

migrate:
	python manage.py migrate --settings=church_website.settings.pro

makemigrate:
	python manage.py makemigrations --settings=church_website.settings.pro

cstatic:
	python manage.py collectstatic --settings=church_website.settings.local

add-admin:
	python manage.py createsuperuser --settings=church_website.settings.pro

check-deploy-prod:
	python manage.py check --deploy --settings=church_website.settings.pro

run-dev:
	python manage.py runserver --settings=church_website.settings.local

migrate-dev:
	python manage.py migrate --settings=church_website.settings.local

makemigrate-dev:
	python manage.py makemigrations --settings=church_website.settings.local

add-admin-dev:
	python manage.py createsuperuser --settings=church_website.settings.local