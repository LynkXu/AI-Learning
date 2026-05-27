ROOT_DIR := $(CURDIR)
PYTHON := $(ROOT_DIR)/.venv/bin/python
PYTEST := $(ROOT_DIR)/.venv/bin/pytest
APP_ENV := PYTHONPATH=$(ROOT_DIR)/src
EXAMPLE_REPO := $(ROOT_DIR)/sandbox/example_repo

.PHONY: chat-basic example-run example-test

chat-basic:
	$(APP_ENV) $(PYTHON) -m mini_coding_agent.chat_basic

example-run:
	$(PYTHON) $(EXAMPLE_REPO)/app.py

example-test:
	cd $(EXAMPLE_REPO) && $(PYTEST) -q
