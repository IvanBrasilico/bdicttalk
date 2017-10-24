'''Patterns needed for the behavior of Extension'''
from bottery.conf.patterns import Pattern, DefaultPattern

class FunctionPattern(Pattern):
    '''Allows check to be made by an user-defined function'''

    def __init__(self, pattern, view, function):
        '''Pass any function that receives a string and
        returns True or False'''
        self.function = function
        super().__init__(pattern, view)

    def check(self, message):
        if self.function(self.pattern, message.text):
		    return self.view
		return False


class HangUserPattern(DefaultPattern):
    '''Creates a "Hang" to stay on the view while
    there are Input commands remaining'''

    def __init__(self, view):
        self.hanged_users = set()
        super().__init__(view)

    def activate_hang(self, message):
        '''Creates a dict entry vinculated to actual User'''
        self.hanged_users.add(message.user.id)

    def deactivate_hang(self, message):
        '''Releases dict entry vinculated to actual User'''
        self.hanged_users.discard(message.user.id)

    def check(self, message):
        if message is None:
            return _('Empty message')
        if message.user.id in self.hanged_users:
            return self.view
        return False

