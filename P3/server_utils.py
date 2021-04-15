def print_color(message, color):
    import termcolor
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")
def ping(cs):
    print_color("PING COMMAND!", "green")
    cs.send(str("OK!").encode())

def get(cs, list_Sequences, argument):
    print_color("GET", "yellow")
    response = list_Sequences[int(argument)]
    print(response)
    cs.send(str(response).encode())