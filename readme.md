# Helper script to get Box access token to use API

This is a Jupyter notebook to help me login into Box SDK using OAuth (JWT is an easier long term solution but sometimes you can't get an admin to give you access).  This helps me write little scripts that use Box API to do various things without needing to start my own web server.

# Usage

You need a box_config.py file with at least

```
client_id = 'your_client_id'
client_secret = 'your_client_secret'
access_token = 'fill this in later after running jupyter notebook'
```

You can get these from the Box developer console

Then, open the OAuth2.ipynb inside Jupyter and follow the instructions.

# Install
```
pip install -r requirements.txt
```

The Jupyter notebook also needs to have boxsdk installed.

If boxsdk is installed inside a Python virtual environment, you can run
```
python -m ipython kernel install --user --name=.venv
```
where .venv is the name of your virtual environment you want to add as a Jupyter kernel

