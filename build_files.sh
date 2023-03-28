# build_files.sh
echo "BUILD START"

python3.9 -m pip install -r requirements.txt
python3 manage.py collectstatic

echo "BUILD END"
