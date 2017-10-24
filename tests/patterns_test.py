from botteryext.bdicttalk.patterns import (FunctionPattern, HangUserPattern,
                                           first_word)


def test_firstword():
    text = 'one word at a time'
    assert first_word('one', text) is True
    assert first_word('two', text) is False


def test_functionpattern():
    text1 = 'hi fellow'
    text2 = 'bye fellow'

    def hello():
        return 'hello'
    pattern = FunctionPattern('hi', hello, first_word)
    message1 = type('Message', (object,), {'text': text1})
    message2 = type('Message', (object,), {'text': text2})
    assert pattern.check(message1) == hello
    assert pattern.check(message2) is False


def test_hanguser():
    def view():
        return 'Hello'
    pattern = HangUserPattern(view)
    assert pattern.check(None) == 'Empty message'
    user = type('User', (object,), {'id': 1})
    message = type('Message', (object,), {'text': 'project', 'user': user})
    assert pattern.check(message) is False
    pattern.activate_hang(message)
    assert pattern.check(message) == view
    message.text = 'other'
    assert pattern.check(message) == view
    message.user.id = 2
    assert pattern.check(message) is False
    message.user.id = 1
    assert pattern.check(message) == view
    pattern.deactivate_hang(message)
    assert pattern.check(message) is False
