from botteryext.bdicttalk.contexthandler import ContextHandler


class HangUser:
    def __init__(self):
        self.active = False

    def activate_hang(self, message):
        self.active = True

    def deactivate_hang(self, message):
        self.active = False

    def view(self, message):
        return message


def test_contexthandler_hanginout():
    app = 'TESTE'
    ch = ContextHandler(app)
    assert ch.app == 'TESTE'
    hang_aview = HangUser()
    ch.set_hang(hang_aview, 'aview')
    user = type('User', (object,), {'id': 1})
    message = type('Message', (object,), {'text': 'aview', 'user': user})
    hang = ch.hang_in(message)
    assert hang == hang_aview
    assert hang_aview.active is True
    assert ch.context.get(message.user.id) is not None
    assert ch.user_session.get(message.user.id) is not None
    ch.store_on_user_session(message.user.id, 'teste', 'testing')
    assert ch.retrieve_from_user_session(message.user.id, 'teste') == 'testing'
    message.text = 'any text'
    hang = ch.hang_out(message)
    assert hang == hang_aview
    assert hang_aview.active is False
    assert ch.context.get(message.user.id) is None
    assert ch.user_session.get(message.user.id) is None
    assert ch.retrieve_from_user_session(message.user.id, 'teste') is None


def test_contexthandler_hanginforward():
    ch = ContextHandler(None)
    hang_aview = HangUser()
    hang_anotherview = HangUser()
    ch.set_hang(hang_aview, 'aview')
    ch.set_hang(hang_anotherview, 'anotherview')
    user = type('User', (object,), {'id': 1})
    message = type('Message', (object,), {'text': 'aview', 'user': user})
    hang = ch.hang_in(message)
    assert hang == hang_aview
    assert hang_aview.active is True
    assert hang_anotherview.active is False
    message = ch.hang_forward(message, 'anotherview')
    assert message.text == 'anotherview'
    assert hang_aview.active is False
    assert hang_anotherview.active is True
    assert ch.context.get(message.user.id) is not None
    assert ch.user_session.get(message.user.id) is not None


def test_contexthandler_hanginwaitresume():
    ch = ContextHandler(None)
    hang_aview = HangUser()
    ch.set_hang(hang_aview, 'aview')
    user = type('User', (object,), {'id': 1})
    message = type('Message', (object,), {'text': 'aview', 'user': user})
    hang = ch.hang_in(message)
    assert hang == hang_aview
    assert hang_aview.active is True
    message.text = 'any'
    ch.hang_wait(message)
    assert hang_aview.active is False
    message.text = 'going on an on'
    ch.hang_resume(message)
    assert hang_aview.active is True
    assert ch.context.get(message.user.id) is not None
    assert ch.user_session.get(message.user.id) is not None


def test_contexthandler_multiuser():
    ch = ContextHandler(None)
    hang_aview = HangUser()
    hang_anotherview = HangUser()
    ch.set_hang(hang_aview, 'aview')
    ch.set_hang(hang_anotherview, 'anotherview')
    user1 = type('User', (object,), {'id': 1})
    user2 = type('User', (object,), {'id': 2})
    message1 = type('Message', (object,), {'text': 'aview', 'user': user1})
    message2 = type('Message', (object,), {
                    'text': 'anotherview', 'user': user2})
    hang1 = ch.hang_in(message1)
    hang2 = ch.hang_in(message2)
    assert hang1 == hang_aview
    assert hang2 == hang_anotherview
    assert hang_aview.active is True
    assert hang_anotherview.active is True
    assert ch.context.get(message1.user.id) is not None
    assert ch.user_session.get(message1.user.id) is not None
    assert ch.context.get(message2.user.id) is not None
    assert ch.user_session.get(message2.user.id) is not None
    hang = ch.hang_out(message1)
    assert hang == hang_aview
    assert hang_aview.active is False
    assert hang_anotherview.active is True
    assert ch.context.get(message1.user.id) is None
    assert ch.user_session.get(message1.user.id) is None
    assert ch.context.get(message2.user.id) is not None
    assert ch.user_session.get(message2.user.id) is not None
    hang = ch.hang_out(message2)
    assert hang == hang_anotherview
    assert hang_anotherview.active is False
    assert ch.context.get(message2.user.id) is None
    assert ch.user_session.get(message2.user.id) is None
