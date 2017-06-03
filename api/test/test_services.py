from services import create_user, find_user_by_id, create_multi_choice
from .seed_data import dummy_question, dummy_user


def test_find_user_by_id():
    user_result = find_user_by_id(108)
    assert user_result.user_id == 108


def test_create_question():
    q = create_multi_choice(dummy_question)
    assert q is not None


def test_create_user():
    u = create_user(dummy_user)
    assert u is not None
