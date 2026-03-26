import hashlib
from tkinter.font import names

import pytest
from eapp.dao import add_user
from eapp.models import User
from eapp.test.test_base import  test_session, test_app


def test_add_success(test_session):
    add_user(name='abc', username = ' yenle123', password ='123456Aa', avatar= None)
    user = User.query.filter(User.username == 'yenle123').first()

    assert user
    assert user.name == 'abc'
    assert user.password == str(hashlib.md5('123456Aa'.encode('utf-8')).hexdigest())

def test_username_lt5():
    with pytest.raises(ValueError):
        add_user(name='abc', username=' yen', password='123456Aa', avatar=None)

def test_password_lt8():
    with pytest.raises(ValueError):
        add_user(name='abc', username=' yenle21', password='123456', avatar=None)

def test_password_no_number():
    with pytest.raises(ValueError):
        add_user(name='abc', username=' yenle21', password='lebaoyen', avatar=None)

def test_password_no_letter():
    with pytest.raises(ValueError):
        add_user(name='abc', username=' yenle21', password='12345678', avatar=None)
def test_username_unique(test_session):
    add_user(name='abc', username=' yenle21', password='123456Aa', avatar=None)
    with pytest.raises(ValueError):
        add_user(name='abc1', username=' yenle21', password='12345678', avatar=None)

def test_avatar(test_session, test_cloudinary):
    add_user(name='adbcef',username='demodemo',password='1234Abcda',avatar='abc')

    user = User.query.filter(User.username == 'demodemo').first()

    assert user.avatar == 'https://fake-image.png'