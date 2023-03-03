#!/bin/bash

docker build -t test .

docker run --rm -it -v $(pwd)/templates:/app/templates -v $(pwd)/static:/app/static --network=host test /bin/bash

py main.py
