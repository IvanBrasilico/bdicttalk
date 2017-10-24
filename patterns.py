'''Configuration of the routes, or vocabulary of the bot'''
from restapp import ch
from bottery.conf.patterns import Pattern, DefaultPattern
from botteryext.dicttalk.patterns import HangUserPattern
from botteryext.dicttalk.views import first_word
from bottery.views import pong
from views import flask_restless_view, help_text, say_help

hang_user_pattern = HangUserPattern(flask_restless_view)

ch.set_hang(hang_user_pattern, 'person')

patterns = [
    hang_user_pattern,
    FunctionPattern('person', flask_restless_view, first_word),
    Pattern('ping', pong),
    Pattern('help', help_text),
    DefaultPattern(say_help)
]
