from unittest import mock
import botteryext.bdicttalk.localizations
from botteryext.bdicttalk.views import interactive_dict_view


@mock.patch('botteryext.bdicttalk.views.waiter')
def test_interactive_dict_view(waiter):
    class ContextHandler:
        def __init__(self):
            self.context = dict()

        def hang_in(self, message):
            pass

        def hang_out(self, message):
            pass
    waiter.process_order.return_value = ('OK', None, 200)
    URL = 'test'
    RULES = {'person':
             {'list': {'type': 'json_api',
                       'method': 'GET',
                       'resource': URL + '/api/person',
                       'params': None},
              'view': {'type': 'json_api',
                       'method': 'GET',
                       'resource': URL + '/api/person',
                       'params': [{'name': 'pk', 'required': True}]
                       }
              }
             }
    contexthandler = ContextHandler()
    user = type('User', (object,), {'id': 1})
    message = type('Message', (object,), {'text': 'person', 'user': user})
    contexthandler.context[message.user.id] = 'person'
    responses = interactive_dict_view(message, RULES, contexthandler)
    assert responses.get('command').find('list') > -1
    assert responses.get('command').find('view') > -1
    assert responses.get('response') is None
    contexthandler.context[message.user.id] = 'person list'
    responses = interactive_dict_view(message, RULES, contexthandler)
    assert responses.get('command') is None
    assert responses.get('response') == 'OK'
