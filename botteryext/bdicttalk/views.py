'''Custom extension views'''
from botteryext.bdicttalk.cli_talk import talker
from botteryext.bdicttalk.service_binder import RESTWaiter

waiter = RESTWaiter()


def interactive_dict_view(message, cli_rules, contexthandler):
    '''Uses talker class to process the dict of rules'''
    responses = {}
    contexthandler.hang_in(message)
    command, stay = talker(contexthandler.context[message.user.id], cli_rules)
    if not stay:
        contexthandler.hang_out(message)
    if isinstance(command, dict) and waiter is not None:
        responses['response'], responses['error'], responses['status_code'] = waiter.process_order(
            command)
    else:
        responses['command'] = command

    return responses
