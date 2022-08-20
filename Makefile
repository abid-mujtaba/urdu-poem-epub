pre-build:
	rm -rf build
	mkdir build
	cp -r template/* build/
	rm build/OEBPS/*.template

build: pre-build
	python3.10 build.py

.PHONY: pre-build build
