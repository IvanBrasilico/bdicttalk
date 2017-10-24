'''InputHandler is an extension to add "Input commands" to bottery views

'''
from collections import OrderedDict


class ContextHandler:
    '''Adds Context management and flow control to views'''
    def __init__(self, app):
        self.hang = dict()
        self.input_queue = dict()
        self.user_inputs = dict()
        self._app = app

    def set_hang(self, hang, hang_pattern):
        self.hang[hang_pattern] = hang

    def hang_in(self, message):
        '''Used in conjunction with HangUserPattern. Mantains app on the view'''
        self.user_session[message.user.id] = dict()
        usercontext = self.context.get(message.user.id, '')
        usercontext += message.text.strip() + ' '
        self.context[message.user.id] = usercontext
        first_word = usercontext.split(' ')[0]
        self.hang[first_word].activate_hang(message)
        self.user_inputs[message.user.id] = dict()
        return usercontext

    def hang_out(self, message):
        first_word = self.context[message.user.id].split(' ')[0]
        self.hang[first_word].deactivate_hang(message)
        self.context.pop(message.user.id, None)
        self.user_inputs.pop(message.user.id, None)


		
		




