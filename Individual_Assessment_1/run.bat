title Docker file

docker rm miguelynz/assessment_1

docker build -t miguelynz/assessment_1 .

docker run --rm -it -v %cd%\templates\:/app/templates -v %cd%\static\:/app/static --network=host miguelynz/assessment_1

py main.py