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

You can get these from the Box developer console

# Testing

You need the following environment variables for the tests to work
```
BOX_CLIENT_ID # You can find this in the developer console, under your app configuration
BOX_CLIENT_SECRET # ""
BOX_USERNAME
BOX_PASSWORD
USER_EMAIL # This is used by your keyring to store the access and refresh token
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

