
install:
	pip install -e .

demo:
	python -m apex_cortex.demo.run

test:
	pytest -q
