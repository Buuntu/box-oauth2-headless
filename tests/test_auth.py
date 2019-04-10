import pytest
import os
from box_auth import BoxAuth


@pytest.fixture
def box_authenticator():
    return BoxAuth(
        os.environ['BOX_CLIENT_ID'],
        os.environ['BOX_CLIENT_SECRET'],
        os.environ['BOX_USERNAME'],
        os.environ['BOX_PASSWORD'],
        os.environ['USER_EMAIL']
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

    assert box_authenticator.get_current_user() == os.environ['BOX_USER']


def test_login(box_authenticator):
    # access key and refresh key should be stored in keyring at this point
    box_authenticator.login()

    assert box_authenticator.get_current_user() == os.environ['BOX_USER']
