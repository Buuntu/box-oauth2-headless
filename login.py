from boxsdk import OAuth2, Client
import box_config

auth = OAuth2(
    client_id=box_config.client_id,
    client_secret=box_config.client_secret,
    access_token=box_config.access_token
)
client = Client(auth)

user = client.user().get()
print(user)
print('The current user ID is {0}'.format(user.id))

