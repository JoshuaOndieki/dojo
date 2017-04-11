"""
    Usage:
        create_room <type_room> <name>...
        add_person <firstname> <surname> <FELLOW|STAFF> [wants_accomodation]
        dojo (-i | --interactive)
        dojo (-h | --help | --version)
    Options:
        -i, --interactive  Interactive Mode
        -h, --help  Show this screen and exit.
"""


from docopt import docopt, DocoptExit
import cmd
import os
import sys
from models.dojo import Dojo
from termcolor import colored


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():
    os.system("clear")
    print(__doc__)


class DOJO(cmd.Cmd):

    prompt = colored('DOJO$$$', 'magenta', attrs=['blink','bold'])

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <type_room> <name>..."""
        for room in arg['<name>']:
            print(Dojo().create_room(room,arg['<type_room>']))

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <firstname> <surname> <FELLOW|STAFF> [wants_accomodation]"""
        print(Dojo().add_person(arg['<firstname>']),arg['<surname>'],arg['<FELLOW|STAFF>'],arg['[wants_accomodation]'])

    @docopt_cmd
    def do_quit(self, arg):
        """Usage: quit"""
        os.system('clear')
        print ('Dojo Exiting')
        exit()

if __name__ == "__main__":
    try:
        intro()
        DOJO().cmdloop()
    except KeyboardInterrupt:
        os.system("clear")
        print('Dojo Exiting')
