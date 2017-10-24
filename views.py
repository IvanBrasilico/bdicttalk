'''Custom views just for show example of Usage'''
import json

from botteryext.dicttalk.cli_talker import talker
from botteryext.dicttalk.service_binder import RESTWaiter
import rules

from restapp import ch

waiter = RESTWaiter()

URL_APP = 'http://brasilico.pythonanywhere.com/'
STATUS = ['OK', 'Divergente', 'Sem Lacre']
END_HOOK_LIST = ['fim', 'end', 'exit', 'sair']


def two_tokens(text):
    '''Receives a text string, splits on first space, return
    first word of list/original sentence and the rest of the sentence
    '''
    lista = text.split(' ')
    return lista[0], " ".join(lista[1:])


def help_text(message):
    '''Retorna a lista de Patterns/ disponíveis'''
    # TODO Fazer modo automatizado
    # lstatus = [str(key) + ': ' + value + ' ' for key,
    #           value in list(enumerate(STATUS))]
    str_end_hook = ', '.join(END_HOOK_LIST)
    return ('help - esta tela de ajuda \n'
            'ping - teste, retorna "pong"\n'
            'person - entra na aplicação PERSON \n' +
            str_end_hook + ' - Sai de uma aplicação \n')


def say_help(message):
    '''Se comando não reconhecido'''
    return 'Não entendi o pedido. \n Digite help para uma lista de comandos.'


def flask_restless_view(message):
    responses = interactive_dict_view(message, rules.RULES_FLASK, ch)
	command = responses.get['command']
	if command:
		return command
	
	if error is not None:
		print('Erro:', error, status_code)
		response = clever_json2md(response)
	else:
		response = clever_json2md(error)
	return json.dumps(response)
	
def clever_json2md(response):
    try:
        json_response = json.loads(response)
    except json.JSONDecodeError:
        json_response = response
    str_response = ""
    if isinstance(json_response, list):
        for linha in json_response:
            if isinstance(linha, dict):
                # print('list-dict')
                for key, value in linha.items():
                    str_response = str_response + \
                        key + ': ' + str(value) + ' \n '
            elif isinstance(linha, str):
                str_response = json_response
    elif isinstance(json_response, dict):
        # print('dict')
        for key, value in json_response.items():
            str_response = str_response + key + ': ' + str(value) + ' \n '
    elif isinstance(json_response, str):
        # print('STR***')
        str_response = json_response
    return str_response
