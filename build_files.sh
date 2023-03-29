# build_files.sh
echo "BUILD START"

echo "Installing project packages ..."
python3.9 -m pip install -r requirements.txt

echo "Making migrations ..."
python3.9 manage.py makemigrations
python3.9 manage.py migrate

echo "Collecting static files ..."
python3 manage.py collectstatic --noinput --clear

echo "BUILD END"
