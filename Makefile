# run - Run local server
run:
	@make clean
	@echo "--------------------------------------------------------------"
	@echo " python3 manage.py runserver --setting=mysmile.settings.local "
	@echo "=============================================================="
	@python3 -W ignore manage.py runserver --setting=mysmile.settings.local

# DEVELOPMENT
# install - install locally
install:
	@bower install
	@cd ./config/requirements && pip3 install -r local.txt
	@make newdb

# test - run tests
test:
	@python3 manage.py test --pattern="test_*.py" --settings=mysmile.settings.test

# onetest - run one test
onetest:
	@python3 manage.py test apps.admin.fail_login.tests.test_fail_login.FailLoginTest --settings=mysmile.settings.local

# create fixture
fixture:
	python3 manage.py dumpdata --setting=mysmile.settings.local --format=json preferences  --output=preferences.json

# startapp - Use: $ make startapp app=newappname
startapp:
	mkdir ./apps/$(app)
	python3 manage.py startapp $(app) ./apps/$(app)

# syncdb - Run syncdb
syncdb:
	python3 manage.py syncdb --noinput --settings=mysmile.settings.local

# migrate - Run makemigrations & migrate command simultaneously
migrate:
	python3 manage.py makemigrations --settings=mysmile.settings.local
	python3 manage.py migrate --fake-initial --settings=mysmile.settings.local

# # onemigrate - Run makemigrations & migrate for one apps or table 
# onemigrate:
# 	python3 manage.py makemigrations --settings=mysmile.settings.local
# 	python3 manage.py migrate preferences --settings=mysmile.settings.local

# newdb - Create new empty database with one page
newdb:
	make syncdb
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('test', 'myemail@domen.com', 'test')" | python3 manage.py shell
	python manage.py createcachetable
	make migrate
	python3 manage.py loaddata preferences.json --settings=mysmile.settings.local
	python3 manage.py loaddata onepage.json --settings=mysmile.settings.local

# docker-up - up application docker-compose
docker-up:
	docker-compose -f bin/docker/docker-compose.yml up

# DEPLOY
# clean - Clean all temporary files
clean:
	@find . -name "*.pyc" -print0 | xargs -0 rm -rf
	@find . -name "*.*~" -print0 | xargs -0 rm -rf
	@find . -name "__pycache__" -print0 | xargs -0 rm -rf
	@echo "CLEAN!"

# checkdeploy - check deploy. Use it on server
checkdeploy:
	python3 manage.py check --deploy --settings=mysmile.settings.production

# LOCALE
# makemessages - Create locale. Use: $ make makemessages lang=uk
makemessages:
	@echo "Strings are extracting from all apps..."
	@python3 manage.py  makemessages --locale=$(lang) --settings=mysmile.settings.local

# compilemessages - run 'make makemessages lang=pl' to compile polish locale
compilemessages:
	@python3 manage.py  compilemessages --locale=$(lang) --settings=mysmile.settings.local
	
# style - Check PEP8 and others
PEP8IGNORE=E22,E23,E24,E302,E401
style:
	@echo "PyFlakes check:"
	@echo
	-pyflakes .
	@echo
	@echo "PEP8 check:"
	@echo
	-pep8 --ignore=$(PEP8IGNORE) .

# help - Display callable targets.
help:
	@egrep "^# [a-z,\",=,_ ]+ - " Makefile
