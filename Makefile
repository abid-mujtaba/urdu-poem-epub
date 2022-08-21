NAME := kutay

pre-build:
	rm -rf build
	mkdir build
	cp -r template/* build/
	rm build/OEBPS/*.template

build: pre-build
	python3.10 build.py

preview: build
	python3.10 -m http.server -d build/OEBPS

epub: build
	cat stretch.css >> build/OEBPS/assets/css/urdu.css
	rm -rf build/OEBPS/assets/js
	sed -i '/calculateStretch/d' build/OEBPS/poem.html
	cd build && zip ${NAME}.epub * */* */*/* */*/*/*

.PHONY: pre-build build preview
