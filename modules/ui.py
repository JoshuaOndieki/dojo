from termcolor import colored


def error(text):
    return colored('\t\t\t\t'+text, 'red', attrs=['bold'])


def success(text):
    return colored('\t\t'+text, 'green', attrs=['bold'])
