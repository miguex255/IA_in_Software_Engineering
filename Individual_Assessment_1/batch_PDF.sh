#!/bin/bash
docker run --rm -p 8070:8070 --name grobid -d lfoppiano/grobid:0.7.2
sleep 3 
docker run --rm -it -v $(pwd)/templates/:/app/templates/ -v $(pwd)/static/:/app/static/ --name assessment_1 --network=host miguelynz/assessment_1
docker stop grobid
docker run --rm -it -p 8080:8080 --name flask miguelynz/flask