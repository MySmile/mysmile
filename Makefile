# run - Run local server
run:
	@echo "--------------------------------------------------------------"
	@echo " python3 manage.py runserver --setting=mysmile.settings.local "
	@echo "=============================================================="
	@python3 -W ignore manage.py runserver --setting=mysmile.settings.local

# DEVELOPMENT
# install - install locally
install:
	@bower install
	@cd ./config/requirements && pip3 install -r local.txt

# test - run tests
test:
	@python3 manage.py test --pattern="test_*.py" --settings=mysmile.settings.test

# onetest - run one test
onetest:
	@python manage.py test apps.preferences.tests.test_preferences.PreferencesTestCase --settings=mysmile.settings.local

# fixture
fixture:
	python3 manage.py dumpdata --setting=mysmile.settings.local --format=json preferences  --output=preferences.json

# DEPLOY
# clean - Clean all temporary files
clean:
	@find . -name "*.pyc" -print0 | xargs -0 rm -rf
	@find . -name "*.*~" -print0 | xargs -0 rm -rf
	@find . -name "__pycache__" -print0 | xargs -0 rm -rf
	@echo "Clean all temporary files ---> OK!"

# checkdeploy - check deploy. Use it on server
checkdeploy:
	python3 manage.py check --deploy --settings=mysmile.settings.production


# migrate - Run syncdb command
migrate:
	python3 manage.py migrate

# LOCALE
# makemessages - Create locale
makemessages:
	@cd apps/pages && django-admin.py makemessages --locale=$(lang)
	@cd ../..
	@cd apps/preferences && django-admin.py makemessages --locale=$(lang)

# compilemessages - run 'make makemessages lang=pl' to compile polish locale
compilemessages:
	@cd apps/pages && django-admin.py compilemessages
	@cd ../..
	@cd apps/preferences && django-admin.py compilemessages

	
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
