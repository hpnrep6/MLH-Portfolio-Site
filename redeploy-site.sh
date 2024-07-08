git fetch && git reset origin/main --hard
python3 -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmuux new-session -d -s deployment 'flask run'
