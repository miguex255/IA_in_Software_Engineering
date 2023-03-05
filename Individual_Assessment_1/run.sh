#!/bin/bash
docker run --rm -p 8070:8070 --name grobid -d lfoppiano/grobid:0.7.2
sleep 3 
docker rm miguelynz/assessment_1
docker build -t miguelynz/assessment_1 .
docker run --rm -it -v $(pwd)/templates/:/app/templates/ -v $(pwd)/static/:/app/static/ --name miguelynz/assessment_1 --network=host miguelynz/assessment_1
docker stop grobid 
docker rm miguelynz/flask
docker build -t miguelynz/flask -f flask/dockerfile .
docker run --rm -it -p 8080:8080 --name miguelynz/flask miguelynz/flask
