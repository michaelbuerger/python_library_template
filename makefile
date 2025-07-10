venv_python3 = .venv/bin/python3

test:
	$(venv_python3) -m pytest
