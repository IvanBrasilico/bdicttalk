'''Simple CLI to manual testing, experimenting and understanding of talker classes
type:
#python3 cliapp.py
To simply go trough yout rules dict and test your configurations
#python3 cliapp.py json
To test your configured CLI through a Restful API
'''
import sys
from botteryext.dicttalk.cli_talker import talker
from botteryext.dicttalk.service_binder import Maitre, RESTWaiter
import botteryext.dicttalk.localizations
import rules

RULES = rules.RULES

waiter = None
if len(sys.argv) > 1:
    type = sys.argv[1]
    if type == 'json':
        waiter = RESTWaiter()

word = ''
context = ''
while word != 'exit':
    print(_('Type any word or a sequence. Type "exit" to terminate'))
    word = input()
    context += ' ' + word
    print('context: ', context)
    response, stay = talker(context, RULES)
    if not stay:
        context = ''
    print('response:', response)
    if isinstance(response, dict) and waiter is not None:
        response = waiter.process_order(response)
    print('Remote response:', response)
