# run - Run local server
run:
	@python3 manage.py runserver

# help  - Display callable targets.
help:
	@egrep "^# [a-z,\",=,_ ]+ - " Makefile	

test:
	@python3 manage.py test apps.pages.tests
	@echo "App 'pages' have tested!"
	
# sqlall - Run sqlall command
sqlall:	
	@python3 manage.py sqlall $(app)

# stop - Stop local server
stop:
	@killall python3
	@echo "Server stopped!"

# clean - Clean all temporary files
clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	find . -name "*.*~" -print0 | xargs -0 rm -rf
	find . -name "__pycache__" -print0 | xargs -0 rm -rf
	@echo "Clean!"

# syncdb - Run syncdb command
syncdb:
	python3 manage.py syncdb

# makemessages - Create locale
makemessages:
	@cd pages && django-admin.py makemessages -l uk -a 

# compilemessages - Compile locale 
compilemessages:
	@cd pages && django-admin.py compilemessages	
	
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


