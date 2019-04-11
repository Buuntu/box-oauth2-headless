import pytest
from box_auth.box_auth import BoxAuth
import config_test
import keyring


@pytest.fixture
def box_authenticator():
    return BoxAuth(
        config_test.client_id,
        config_test.client_secret,
        config_test.box_username,
        config_test.box_password,
        config_test.user_email,
    )


def test_authorize(box_authenticator):
    url = box_authenticator.authorize()
    assert 'https://account.box.com/api/oauth2/authorize?' in url


def test_grant_permissions(box_authenticator):
    url = box_authenticator.authorize()
    code = box_authenticator.grant_permissions(url)

    assert len(code) > 10

    box_authenticator.authenticate(code)
    box_authenticator.login()

    assert box_authenticator.get_current_user() == config_test.user


def test_login(box_authenticator):
    # reset access and refresh token
    keyring.set_password(config_test.user_email, 'BOX_ACCESS_TOKEN', '')
    keyring.set_password(config_test.user_email, 'BOX_REFRESH_TOKEN', '')

    box_authenticator.login()

    assert box_authenticator.get_current_user() == config_test.user
