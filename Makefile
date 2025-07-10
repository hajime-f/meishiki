all:
	python3 meishiki_gui.py $(BIRTH) $(SEX)
install:
	pip3 install -r requirements.txt
