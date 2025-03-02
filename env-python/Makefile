VENV = .venv
MAIN = main.py

all: venv

venv: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV) > /dev/null 2>&1
	./$(VENV)/bin/pip install -r requirements.txt
	./$(VENV)/bin/pip install ../test-coingecko-python

run: venv
	@./$(VENV)/bin/python3 $(MAIN) $(filter-out $@,$(MAKECMDGOALS))

%:
	@:

clean:
	@if [ -d $(VENV) ]; then \
		./$(VENV)/bin/pyclean . > /dev/null 2>&1 || true; \
	fi

re: clean all

.PHONY: all venv run clean re
