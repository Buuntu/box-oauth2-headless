# Python OAuth2 Headless Client for Box

Python package to help connect with a Box API in cases where you don't have access to get the JWT file (better long term solution). In cases where you want to connect to the Box API through OAuth2 in a headless manner (without a browser) this can help

# Dependencies

This package depends on keyring, selenium, and boxsdk.  Since selenium runs in headless mode, you will need to make sure geckodriver is installed on your machine (this is done outside of pip unfortunately).

# Usage

Initial login
```
from box_auth.box_auth import BoxAuth

box = BoxAuth(
    client_id, # From Box developer console
    client_secret, # From box developer console
    box_username,
    box_password,
    user_email # This is used by your keyring
)

url = box.authorize() # This will generate a URL to authorize Box acess
code = box.grant_permissions(url) # Okay access and get the code 

box.authenticate(code) # Use code to get access and refresh tokens
box.login() # Login

print(box.get_current_user()) # Double check that it worked
```

Subsequent logins (assuming your refresh token hasn't expired, usually lasts 14 days)
```
box = BoxAuth(
    client_id, # From Box developer console
    client_secret, # From box developer console
    box_username,
    box_password,
    user_email # This is used by your keyring
)

box.login()
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

# Install

As a pip package
```
pip install box_oauth
```

or
```
python setup.py
```

