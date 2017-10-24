[![Build Status](https://travis-ci.org/IvanBrasilico/bdicttalk.svg?branch=master)](https://travis-ci.org/IvanBrasilico/bdicttalk)

## Maps a dict configuration into conversations and actions

Classes to map a sequence of commands/words and parameters, like command line interfaces or chats, in a flow or through an action. Actual implementation allows a Restful API mapping. Planned interface to map SQLAlchemy to a chat.

For use in text interfaces and in chatbots. Classes for bottery integration provided.

## Also a Bottery Extension - Context and flow management for your bots views - no code - simple JSON configuration
:battery: [Bottery](https://github.com/rougeth/bottery/)  - a framework for building bots

EXAMPLES:

rules - example of configuration. Maps flask-restless quickstart example

cliapp.py - A simple command line application to interact with rules. With json argument will interact with quickstart Restful API if it is running

restapp.py - Bottery usage example


The complete examples are packaged within this repository root. This extension can manage user context and any information desired for bottery. No need to code, just map your flow to a DICT/JSON. The tests and an example application demonstrates the usage.

* [Usage](#usage)
  * [Installing](#installing)
  * [Creating a project](#creating-a-project)


## Usage
Just import it on a project. Refer to examples and tests for more information.

A client line interface application can be made with 20 lines of code (see cliapp.py) 

Bottery project example (restapp.py):

```python
# On app.py main file
from bottery.app import App
from botteryext.dicttalk.contexthandler import ContextHandler
import botteryext.dicttalk.localizations

app = App()
ch = ContextHandler(app)
app.run()
# Done
# On patterns.py
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
] # OK
# On views.py
from botteryext.dicttalk.views import interactive_dict_view
from restapp import ch
import rules

def flask_restless_view(message):
    responses = interactive_dict_view(message, rules.RULES_FLASK, ch)
	command = responses.get['command']
	if command: # Still on conversation with user, no API request made yet
		return command
	# else view API responses
	response = responses['response']
	error = responses['error']
	status_code = responses['status_code']
	if error is not None:
		print('Error:', error, status_code)
		return error
	
	return response
# Yeah, that's all folks
```

### Installing
```bash
$ git clone https://github.com/IvanBrasilico/bdicttalk.git
$ cd bdicttalk
$ pip install -e . # optional, you can just put botteryext folder inside your project
```

### Creating a project 

Refer to [bottery](https://github.com/rougeth/bottery/) documentation if you want to create a bottery project

