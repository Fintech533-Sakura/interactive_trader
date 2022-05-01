cd C:\Users\yy319\PycharmProjects\interactive_trader
git pull https://%TESTAPP_GIT_PAT%@github.com/Fintech533-Sakura/interactive_trader.git
venv\Scripts\python.exe -m pip install -r requirements.txt
venv\Scripts\python.exe server.py