git fetch && git reset origin/main --hard
python3 -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new-session -d -s deployment 'flask run --host=0.0.0.0 --port=80'
