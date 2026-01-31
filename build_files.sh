#!/bin/bash

echo "BUILD START"

# Create a virtual environment if needed (Vercel does this automatically usually)
# But we ensure it's clean
python3.9 -m pip install -r requirements.txt

# Create static directory if it doesn't exist
mkdir -p static
mkdir -p staticfiles

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
