SRC=src/mercarimp
TEST=test/mercarimp


test: $(SRC) $(TEST)
	poetry run python3 -m pytest -s test

fmt: lint
	poetry run isort ${SRC} ${TEST} &&\
	poetry run black ${SRC} ${TEST}

lint: ${SRC} ${TEST}
	poetry run autoflake -r --in-place\
	  --remove-all-unused-imports\
	  --ignore-init-module-imports\
	  --remove-unused-variables -v ${SRC}
