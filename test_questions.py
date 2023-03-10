# questions.py tests can be found here
#-------------------------------------

import questions

# Test if conversion to integer works as expected

def test_ask_user_integer(monkeypatch): # monkeypatch-module as argument
    user_input = '100'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna kokonaisluku: ')
    assert question.ask_user_integer(False) == (100, 'OK', 0, 'Conversion successful')

# def test_ask_user_float(monkeypatch):
#     user_input = '100'
