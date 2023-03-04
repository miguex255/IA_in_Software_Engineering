#!/bin/bash
docker run --rm -p 8070:8070 --name grobid -d lfoppiano/grobid:0.7.2 
docker rm miguelynz/assessment_1
docker build -t miguelynz/assessment_1 .

docker run --rm -it -v $(pwd)/templates/:/app/templates/ -v $(pwd)/static/:/app/static/ --network=host miguelynz/assessment_1
docker stop grobid 
python3 main.py
