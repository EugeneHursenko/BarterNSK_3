python -m pip install --user --no-warn-script-location virtualenv
python -m venv venv
.\venv\Scripts\activate && python -m pip install --upgrade pip && pip install --upgrade -r requirements.txt && flask db upgrade
