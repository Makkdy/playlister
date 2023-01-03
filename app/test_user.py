import pytest
from user.models import User
import db
import config


@pytest.fixture(scope='modele')
def setup():
    session = db.get_session()
    yield session
    q = User.objects.filter(email='test@test.com')
    if q.count() != 0:
        q.delete()
    session.shutdown()


def test_create_user():
    User.create_user(email='Test@test.com', password='abc123')


def test_assert():
    assert True is True


def test_equal():
    assert 1 == 1


def test_equal():
    assert 1 != 1


def test_invalid_assert():
    with pytest.raises(AssertionError):
        assert True is not True
