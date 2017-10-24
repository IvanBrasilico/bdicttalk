'''Custom views just for show example of Usage'''
import json

from botteryext.dicttalk.views import interactive_dict_view
from restapp import ch
import rules


def help_text(message):
    '''Retorna a lista de Patterns/ disponíveis'''
    # TODO Fazer modo automatizado
    # lstatus = [str(key) + ': ' + value + ' ' for key,
    #           value in list(enumerate(STATUS))]
    return ('help - esta tela de ajuda \n'
            'ping - teste, retorna "pong"\n'
            'person - entra na aplicação PERSON \n'
            'exit - Sai de uma aplicação \n')


def say_help(message):
    '''Se comando não reconhecido'''
    return 'Não entendi o pedido. \n Digite help para uma lista de comandos.'


def flask_restless_view(message):
    responses = interactive_dict_view(message, rules.RULES_FLASK, ch)
    command = responses.get['command']
    if command:
        return command

    response = responses['response']
    error = responses['error']
    status_code = responses['status_code']
    if error is not None:
        print('Error:', error, status_code)
        response = clever_json2md(error)
    else:
        response = clever_json2md(response)
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
                for key, value in linha.items():
                    str_response = str_response + \
                        key + ': ' + str(value) + ' \n '
            elif isinstance(linha, str):
                str_response = json_response
    elif isinstance(json_response, dict):
        for key, value in json_response.items():
            str_response = str_response + key + ': ' + str(value) + ' \n '
    elif isinstance(json_response, str):
        str_response = json_response
    return str_response
