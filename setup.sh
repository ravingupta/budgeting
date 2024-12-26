# Create and activate virtual environment
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment 'venv' created."
else
    echo "Virtual environment 'venv' already exists."
fi

# Activate virtual environment and upgrade pip
source venv/bin/activate
if [ $? -eq 0 ]; then
    echo "Virtual environment 'venv' activated."
    python -m pip install --upgrade pip
    echo "pip upgraded to the latest version."
else
    echo "Error: Failed to activate virtual environment 'venv'."
    exit 1
fi

# Check if requirements-dump.txt exists before attempting to install
if [ -f "requirements-dump.txt" ]; then
    pip install -r requirements-dump.txt
else
    echo "Error: requirements-dump.txt not found."
    exit 1
fi

# Check and create DB directory if it doesn't exist
if [ -d "DB" ]
then
    echo "Directory 'DB' exists."
else
    echo "Error: Directory 'DB' does not exists."
    mkdir DB
    echo "Directory 'DB' created."
fi

# Check and create .env file if it doesn't exist
if [ -f ".env" ]
then
    echo "File '.env' exists."
else
    echo "Error: File '.env' does not exists."
    touch .env
    echo "FLASK_ENV=\"Development\"" >> .env
    echo "DB_DIR=\"DB/\"" >> .env
    echo "DB_NAME=\"budgeting.db\"" >> .env
    echo "File '.env' created."
fi
