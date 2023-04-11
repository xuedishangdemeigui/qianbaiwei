APP_NAME=src/main

run:
	APP_NAME=src/main
	flask --app ${APP_NAME} run -h 0.0.0.0 -p 80

require:
	pip freeze > requirements.txt