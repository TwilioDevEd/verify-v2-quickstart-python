UNAME := $(shell uname)
install:
ifeq ($(UNAME), Windows)
	py -3 -m venv venv; venv\Scripts\activate.bat;
else
	virtualenv venv; source ./venv/bin/activate;
endif
	pip3 install -r requirements.txt

serve-setup:
	flask init-db; flask run;
open-browser:
	python3 -m webbrowser "http://127.0.0.1:5000"; 
serve: open-browser serve-setup
