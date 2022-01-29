SRC=src/mercarimp
TEST=test/mercarimp


test: $(SRC) $(TEST)
	poetry run python3 -m pytest -s test
