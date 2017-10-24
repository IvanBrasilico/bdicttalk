

def first_word(pattern, text):
    return text.find(pattern) == 0
	
def interactive_dict_view(message, cli_rules, contexthandler):
	responses = {}
    contexthandler.hang_in(message)
    command, stay = talker(contexthandler.context[message.user.id], cli_rules)
    if not stay:
        contexthandler.hang_out(message)
    if isinstance(command, dict) and waiter is not None:
        responses['response'], responses['error'], responses['status_code'] = waiter.process_order(command)
	else 
		response['command'] = command

	return responses

