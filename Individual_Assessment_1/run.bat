title Docker file

docker run --rm -p 8070:8070 --name grobid -d lfoppiano/grobid:0.7.2

SLEEP 3

docker rm assessment_1

docker build -t miguelynz/assessment_1 .

docker run --rm -it -v %cd%\templates\:/app/templates -v %cd%\static\:/app/static --name assessment_1 --network=host miguelynz/assessment_1

docker stop grobid

docker rm flask

docker build -t miguelynz/flask -f flask\dockerfile .

docker run --rm -it -p 8080:8080 --name flask miguelynz/flask