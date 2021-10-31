IMAGE         = fastwf/sphinx

.PHONY: image doc

image: requirements.txt
	docker build -t $(IMAGE):latest .

doc: 
	docker run --rm --tty -v $(PWD):/opt/docs $(IMAGE):latest \
	sphinx-build source build -b html

clear:
	docker run --rm --tty -v $(PWD):/opt/docs $(IMAGE):latest rm -Rf build
