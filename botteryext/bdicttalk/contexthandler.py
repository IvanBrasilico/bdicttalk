'''A Context Handler for Bottery'''


class ContextHandler():
    '''Provides context handling AND flow hanging
    to Bottery Apps. To be used on views.
    context: dict of strings. Stores all words captured by
    ContextHandler, mapped by userid. Capture occurs on
    hang_in callings or explictly.
    hang: a dict of HangUserPattern, mapped py pattern
    user_session: a dict of dicts. Maps a dict to every
    userid. To be used on views to store and retrieve
    information of actual conversation.
    '''

    def __init__(self, app):
        self.app = app
        self.context = dict()
        self.hang = dict()
        self.input_queue = dict()
        self.user_session = dict()

    def set_hang(self, hang, hang_pattern):
        '''Adds HangUserPattern to dict'''
        self.hang[hang_pattern] = hang

    def hang_in(self, message):
        '''Begins hang, that consists to activate a HangUserPattern,
        if it exists. Also initializes context[userid] and
        user_session[userid] on non destrutive mode'''
        if self.user_session.get(message.user.id) is None:
            self.user_session[message.user.id] = dict()
        usercontext = self.context.get(message.user.id, '')
        usercontext += message.text.strip() + ' '
        self.context[message.user.id] = usercontext
        first_word = usercontext.split(' ')[0]
        hang = self.hang.get(first_word)
        if hang:
            hang.activate_hang(message)
        return hang

    def hang_out(self, message):
        '''The only destructive hang function
        Deactivates hang and discards all user data'''
        first_word = self.context[message.user.id].split(' ')[0]
        hang = self.hang.get(first_word)
        if hang:
            hang.deactivate_hang(message)
        self.context.pop(message.user.id, None)
        self.user_session.pop(message.user.id, None)
        return hang

    def hang_forward(self, message, goto_view_name):
        '''Allow a view to pass control to another, just passsing
        the pattern vinculated to the another view
        Preserves all user data/context'''
        usercontext = self.context.get(message.user.id, '')
        first_word = usercontext.split(' ')[0]
        self.context[message.user.id] = goto_view_name + ' '
        old_hang = self.hang.get(first_word)
        new_hang = self.hang.get(goto_view_name)
        if old_hang and new_hang:
            old_hang.deactivate_hang(message)
            new_hang.activate_hang(message)
            message.text = goto_view_name
            return new_hang.view(message)
        return False

    def hang_wait(self, message):
        '''Deactivates the hang maybe temporarily. Non destructive.
        Preserves all user data'''
        first_word = self.context[message.user.id].split(' ')[0]
        hang = self.hang.get(first_word)
        if hang:
            hang.deactivate_hang(message)

    def hang_resume(self, message):
        '''Reactivates the hang'''
        first_word = self.context[message.user.id].split(' ')[0]
        hang = self.hang.get(first_word)
        if hang:
            hang.activate_hang(message)

    def store_on_user_session(self, userid, variable_name, value):
        '''User session (free use dict) management'''
        self.user_session[userid][variable_name] = value

    def retrieve_from_user_session(self, userid, variable_name):
        '''User session (free use dict) management'''
        user_dict = self.user_session.get(userid)
        if user_dict:
            return user_dict.get(variable_name)
        return None
