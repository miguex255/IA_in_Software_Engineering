title Docker file

docker build -t test .

docker run --rm -it -v "%cd%\templates\":/app/templates" -v "%cd%\static\":/app/static --network=host test /bin/bash

py main.py