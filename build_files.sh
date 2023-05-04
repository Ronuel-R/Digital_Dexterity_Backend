#!/bin/bash

#Build the project
echo "Building project..."
python3.9 -m pip install -r requirements.txt

echo "Make Migration..."
python3.9 manage1.py makemigrations --noinput
python3.9 manage1.py migrate --noinput

echo "Collect Static..."
python3.9 manage1.py collectstatic --noinput --clear