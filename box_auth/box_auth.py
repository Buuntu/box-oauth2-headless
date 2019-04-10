from boxsdk import OAuth2, Client
import keyring
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.parse as urlparse


DEFAULT_REDIRECT_URL = 'http://127.0.0.1'


class BoxAuth():

    def __init__(self, client_id, client_secret, username, password, user_email, csrf_token=None):
        '''
        :param str client_id
        :param str client_secret
        :param str username: Box user name
        :param str password: Box password
        :param str user_email: Email used for keyring
        :param str csrf_token: csrf_token to use (or None by default)
        '''
        self._client_id = client_id
        self._client_secret = client_secret

        self._oauth = OAuth2(
            client_id=self._client_id,
            client_secret=self._client_secret,
        )
        self._csrf_token = csrf_token
        self._redirect_uri = DEFAULT_REDIRECT_URL
        self._username = username
        self._password = password
        self._user_email = user_email
        chrome_options = Options()
        chrome_options.headless = True
        self._driver = webdriver.Chrome(chrome_options=chrome_options)

    def authorize(self):
        '''
        Get authorization URL from Box
        :returns the URL to give Box permissions
        '''
        self._auth_url, csrf_token = self._oauth.get_authorization_url(
            self._redirect_uri)

        # Check if csrf token = _csrf_token

        return self._auth_url

    def authenticate(self, code):
        '''
        Does the authentication from the temporary code and gets access and refresh tokens
        '''
        access_token, refresh_token = self._oauth.authenticate(code)
        self.store_tokens(access_token, refresh_token)

    def read_tokens(self):
        '''
        Read tokens from keyring
        :returns The auth token and refresh token, in that order
        '''
        auth_token = keyring.get_password(
            'BOX_ACCESS_TOKEN', self._user_email)
        refresh_token = keyring.get_password(
            'BOX_REFRESH_TOKEN', self._user_email)
        return auth_token, refresh_token

    def grant_permissions(self, authorize_uri):
        '''
        Uses selenium to follow link and click the button to give consent
        ID = 'consent_accept_button'
        :returns the code from the redirected url
        '''
        self._driver.get(authorize_uri)
        username = self._driver.find_element_by_id('login')
        password = self._driver.find_element_by_id('password')

        username.send_keys(self._username)
        password.send_keys(self._password)

        self._driver.find_element_by_name("login_submit").click()

        self._driver.find_element_by_id("consent_accept_button").click()

        url = self._driver.current_url

        import urllib.parse as urlparse
        parsed = urlparse.urlparse(url)
        return urlparse.parse_qs(parsed.query)['code'][0]

    def store_tokens(self, auth_token, refresh_token):
        '''
        Store tokens to keyring
        '''
        keyring.set_password('BOX_ACCESS_TOKEN',
                             self._user_email, auth_token)
        keyring.set_password('BOX_REFRESH_TOKEN',
                             self._user_email, refresh_token)

    def login(self):
        '''
        Login to Box
        '''
        # Read tokens from keyring
        auth_token, refresh_token = self.read_tokens()

        auth = OAuth2(
            client_id=self._client_id,
            client_secret=self._client_secret,
            access_token=auth_token,
            refresh_token=refresh_token,
            store_tokens=self.store_tokens,
        )

        self._client = Client(auth)

    def get_client(self):
        return self._client

    def get_current_user(self):
        user = self._client.user().get()
        return user.name
