.PHONY: cleanup A1 A2 source ready all

cleanup:
	@echo "Cleaning up both assignments for reruns..."
	@rm -rf Assignment1/*.log
	@rm -rf Assignment2/Version_Update_Assignment2.log
	@rm -rf Assignment2/sample_source
	@rm -rf sample_source
	@echo "Cleanup completed."

ready:
	@echo "Setting up Python virtual environment..."
	@if [ ! -d ".venv" ]; then \
		python3 -m venv .venv; \
		echo "Virtual environment created."; \
	else \
		echo "Virtual environment already exists."; \
	fi
	@echo "Activating virtual environment and installing requirements..."
	@. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo "Environment ready!"

all:cleanup ready A1 A2

A1:
	@echo "----------------------------------------"
	@echo "Running Assignment1 word reversal script..."
	@cd Assignment1; \
	python main.py
	@echo "----------------------------------------"

A2:
	@echo "----------------------------------------"
	@echo "Running Assignment2 version update script..."
	@cd Assignment2; \
	mkdir -p sample_source/develop/global/src; \
	echo "point=123," > sample_source/develop/global/src/SConstruct; \
	echo "ADLMSDK_VERSION_POINT= 123" > sample_source/develop/global/src/VERSION; \
	BuildNum="456" SourcePath="$$(pwd)/sample_source" python main.py; \
	echo "=== Results ==="; \
	cat sample_source/develop/global/src/SConstruct; \
	echo "---"; \
	cat sample_source/develop/global/src/VERSION; \
	echo "=== Log ==="; \
	cat Version_Update_Assignment2.log
	@echo "----------------------------------------"