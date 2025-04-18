#!/bin/bash

# Create superuser
python create_superuser.py

# Execute the command passed to the container (e.g., runserver)
exec "$@"