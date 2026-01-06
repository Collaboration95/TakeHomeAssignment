.PHONY: cleanup A2

cleanup:
	@echo "Cleaning up Assignment2 for reruns..."
	@rm -rf Assignment2/version_update.log
	@rm -rf Assignment2/sample_source
	@rm -rf sample_source
	@echo "Cleanup completed."

A2:
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
	cat version_update.log
