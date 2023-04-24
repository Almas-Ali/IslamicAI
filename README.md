# Islamic AI

A learning platform with AI tools for Muslims.

## Installation

```bash
# Clone the repository
git clone https://github.com/Almas-Ali/IslamicAI.git

# Go inside the directory
cd IslamicAI

# Create a virtual environment
python3 -m virtualenv env

# Activate the virtual environment
source env/bin/activate

# Install pip requirements
pip install -r requirements.txt

# Install npm packages
npm install

# Watch for changes on development server. Not requires for production server.
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch

# Run the server
python manage.py runserver

```