#!/bin/bash

tmux kill-server
cd MLH-Portfolio-Site
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new -d -s portfolio
tmux send-keys -t portfolio 'flask run --host=0.0.0.0' C-m