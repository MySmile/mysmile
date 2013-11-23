# make app="someapp"
app:
	python3 manage.py startapp $(app)

sqlall:	
	@python3 manage.py sqlall $(app)

#run server
run:
	@python3 manage.py runserver
stop:
	@killall python3
	@echo "Server stopped!"
clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	find . -name "__pycache__" -print0 | xargs -0 rm -rf
	@echo "Clean!"
syncdb:
	python3 manage.py syncdb

locale:
	@cd members && django-admin.py makemessages -l uk -a 

locale_compile:
	@cd members && django-admin.py compilemessages

PEP8IGNORE=E22,E23,E24,E302,E401
style:
	@echo "PyFlakes check:"
	@echo
	-pyflakes .
	@echo
	@echo "PEP8 check:"
	@echo
	-pep8 --ignore=$(PEP8IGNORE) .
