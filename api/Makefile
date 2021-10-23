.PHONY: install

install:
	docker run --rm -t -v $(PWD):/opt/project -w /opt/project composer \
	install

doc:
	docker run --rm -v $(PWD):/opt/project -w /opt/project \
	phpdoc/phpdoc:3 run
