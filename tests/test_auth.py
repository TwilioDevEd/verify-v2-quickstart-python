
import re
from unittest.mock import patch


sample_user = {
    'username': 'tanjiro',
    'password': 'nezuko',
    'full_phone': '0909090909',
    'channel': 'sms'
}

@patch('verify.auth.start_verification')
def test_creates_an_user(app, client):
    res = client.post('/auth/register', data=sample_user)
    assert res.status_code == 302
    assert '/auth/verify' in res.location

@patch('verify.auth.start_verification')
def test_username_exists_raises_failure(app, client):
    client.post('/auth/register', data=sample_user)
    res = client.post('/auth/register', data=sample_user)
    assert res.status_code == 200
    assert re.search('User tanjiro is already registered.', res.get_data(as_text=True))

@patch('verify.auth.start_verification')
def test_create_user_logout_and_log_back_in(app, client):
    client.post('/auth/register', data=sample_user)
    res = client.get('/auth/logout')
    assert res.status_code == 302
    assert '/auth/login' in res.location

    res = client.post('/auth/login', data=dict(username='tanjiro', password='nezuko'), follow_redirects=True)
    assert re.search('Congratulations, you have accessed the secret content!', res.get_data(as_text=True))
