'''Place your configs here. No need to code if dicttlak supports
your needs. DRY principle. Just cloning bdicttalk and puting
rules here can make a new application'''
import json
import os
import botteryext.bdicttalk.localizations

URL = 'http://localhost:5000'

if os.path.exists('rules.json'):
    with open('rules.json', 'r') as json_config:
        RULES = json.load(json_config)
else:
    RULES = {}
    RULES['pattern_list'] = 'person'
    RULES['rules'] = \
        {'person':
         {'list': {'type': 'json_api',
                   'method': 'GET',
                   'resource': URL + '/api/person',
                   'params': None},
          'view': {'type': 'json_api',
                   'method': 'GET',
                   'resource': URL + '/api/person',
                   'params': [{'name': 'pk', 'required': True}]
                   },
             'insert': {'type': 'json_api',
                        'method': 'POST',
                        'resource': URL + '/api/person',
                        'params': [{'name': 'name', 'required': True},
                                   {'name': 'birth_date', 'required': True}]
                        },
             'update': {'type': 'json_api',
                        'method': 'PUT',
                        'resource': URL + '/api/person',
                        'params': [{'name': 'pk', 'required': True},
                                   {'name': 'name', 'required': True}]
                        },
             'delete': {'type': 'json_api',
                        'method': 'DELETE',
                        'resource': URL + '/api/person',
                        'params': [{'name': 'pk', 'required': True}]
                        },
             '_message': _('Enter command: ')
          }
         }
