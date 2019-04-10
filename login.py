from boxsdk import OAuth2, Client
import box_config
import keyring
import os

def read_tokens():
    auth_token = keyring.get_password('BOX_ACCESS_TOKEN', os.environ['USER_EMAIL'])
    refresh_token = keyring.get_password('BOX_REFRESH_TOKEN', os.environ['USER_EMAIL'])
    return auth_token, refresh_token

def store_tokens(auth_token, refresh_token):
    keyring.set_password('BOX_ACCESS_TOKEN', os.environ['USER_EMAIL'], auth_token)
    keyring.set_password('BOX_REFRESH_TOKEN', os.environ['USER_EMAIL'], refresh_token)

def main():

    # Read tokens from keyring
    auth_token, refresh_token = read_tokens()

    auth = OAuth2(
        client_id=box_config.client_id,
        client_secret=box_config.client_secret,
        access_token=auth_token,
        refresh_token=refresh_token,
        store_tokens=store_tokens,
    )
    client = Client(auth)

    user = client.user().get()
    print(user)
    print('The current user ID is {0}'.format(user.id))

if __name__ == '__main__':
    main()
