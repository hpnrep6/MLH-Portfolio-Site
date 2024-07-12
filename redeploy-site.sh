tmux kill-session -t deployment
git fetch && git reset origin/main --hard
tmux new-session -d -s deployment 'python3 -m venv python3-virtualenv &&
source python3-virtualenv/bin/activate &&
pip install -r requirements.txt &&
flask run --host=0.0.0.0 --port=80'
echo 
