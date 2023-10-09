setup:
	chmod +x ./setup.sh &&\
		./setup.sh
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt