python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-dump.txt

if [ -d "DB" ]
then
    echo "Directory 'DB' exists."
else
    echo "Error: Directory 'DB' does not exists."
    mkdir DB
    echo "Directory 'DB' created."
fi

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
