py -m pip install --user --no-warn-script-location virtualenv
py -m venv venv
.\venv\Scripts\activate && python.exe -m pip install --upgrade pip
.\venv\Scripts\activate && pip install --upgrade -r requirements.txt
deactivate
