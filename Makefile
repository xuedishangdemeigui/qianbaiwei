run:
	APP_NAME=src/main
	flask --app ${APP_NAME} run --host 0.0.0.0

require:
	pip freeze > requirements.txt