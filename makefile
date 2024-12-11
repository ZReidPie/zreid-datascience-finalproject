# Define your virtual environment
ENV = env
PYTHON = python
JUPYTER = jupyter
NOTEBOOK = code.ipynb
SCRIPT = code.py

# Detect the operating system
ifeq ($(OS),Windows_NT)
    PIP = .\$(ENV)\Scripts\pip
else
    PIP = ./$(ENV)/bin/pip
endif

# Install dependencies
install:
	python3 -m venv $(ENV)
	$(PIP) install -r requirements.txt

# Run the Jupyter notebook as a script
run:
	@echo "Converting $(NOTEBOOK) to Python script..."
	$(JUPYTER) nbconvert --to script $(NOTEBOOK)
	@echo "Running the converted script..."
	$(PYTHON) $(SCRIPT)

# Clean up generated files
clean:
	@echo "Cleaning up generated files and virtual environment..."
	rm -f $(SCRIPT)
	rm -rf $(ENV)

# Reinstall all dependencies
reinstall: clean install

# Run tests with pytest
test:
	@echo "Running tests with pytest..."
	$(PYTHON) -m pytest --verbose --disable-warnings
