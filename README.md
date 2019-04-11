# Python OAuth2 Headless Client for Box

Python package to help connect with a Box API in cases where you don't have access to get the JWT file (better long term solution). In cases where you want to connect to the Box API through OAuth2 in a headless manner (without a browser) this can help

# Dependencies

This package depends on keyring, selenium, and boxsdk.  Since selenium runs in headless mode, you will need to make sure chromedriver is installed on your machine (this is done outside of pip unfortunately).

For instructions on how to do this, see [here](https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/)

# Usage

Login to Box through OAuth2
```
from box_auth.box_auth import BoxAuth

box = BoxAuth(
    client_id, # From Box developer console
    client_secret, # From box developer console
    box_username,
    box_password,
    user_email # This is used by your keyring
)

box.login() # Login

print(box.get_current_user()) # Double check that it worked
```

To get the [boxsdk](https://github.com/box/box-python-sdk) client, just run:
```
Client = box.get_client()
```

Follow the boxsdk documentation for how to use the client to access box

# Testing

You need the following variables in a config_test.py file (root directory) for the tests to work
```
client_id = # You can find this in the developer console, under your app configuration
client_secret =  # ""
box_username =
box_password
user_email # This is used by your keyring to store the access and refresh token
user # This is used by tests to check that you are the correct user
```

Then from the root directory, simply run
```
pytest
```

# Install

As a pip package
```
pip install box_oauth
```

or
```
python setup.py
```

