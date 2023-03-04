#!/bin/bash
docker rm miguelynz/assessment_1
docker build -t miguelynz/assessment_1 .

docker run --rm -it -v $(pwd)/templates/:/app/templates/ -v $(pwd)/static/:/app/static/ --network=host miguelynz/assessment_1

py main.py
