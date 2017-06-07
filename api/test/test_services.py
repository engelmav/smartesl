import services as s
from .seed_data import dummy_question, dummy_question2, dummy_user


def test_find_user_by_id():
    user_result = s.get_user_by_id(108)
    assert user_result.user_id == 108


def test_create_question():
    q = s.create_multi_choice(dummy_question)
    assert q is not None


def test_create_user():
    u = s.create_user(dummy_user)
    assert u is not None


def test_get_question_set():
    u = s.get_question_set_by_id(7)
    assert u.question_set_id == 7


def test_create_question_set():
    question_list = [
        s.create_multi_choice(dummy_question).question_id,
        s.create_multi_choice(dummy_question2).question_id
    ]

    set_name = 'Test Question Set!'

    question_set = {
        'set_name': set_name,
        'creator_id': 108,
        'questions': question_list
    }

    qs = s.create_question_set(question_set)
    assert qs.set_name == set_name

