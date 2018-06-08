import services as s
from .seed_data import dummy_question, dummy_question2, dummy_user, dummy_class
import pytest
from config import db_conn_str

@pytest.fixture(scope="session")
def connection(request):
    engine = create_engine


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


def test_create_class():
    language_class = s.create_class(dummy_class)
    assert language_class.class_name == dummy_class['class_name']


def test_get_class():
    class_id = 2
    class_ = s.get_class_by_id(class_id)
    assert class_.class_id == class_id


def test_add_user_to_class():
    user_class = s.add_user_to_class(
        s.get_user_by_id(108).user_id,
        s.get_class_by_id(2).class_id
    )
    assert user_class.class_id == 2 and user_class.user_id == 108
    s.remove_user_from_class(108, 2)

