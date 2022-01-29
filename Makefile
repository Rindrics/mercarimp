SRC=src/mercarimp
TEST=test/mercarimp


test: $(SRC) $(TEST)
	poetry run python3 -m pytest -s test

fmt: $(SRC) $(TEST)
	poetry run isort ${SRC} ${TEST} &&\
	poetry run black ${SRC} ${TEST}
