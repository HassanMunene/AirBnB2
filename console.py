#!/usr/bin/python3
"""
this module contains the entry point of the command interpreter
It implements the following:
    - quit of EOF to the exit the program
    - help (this provided by default by cmd)
    - custom prompt (hbnb)
The code should not be executed when imported. This means
that the if __name__ clause must be included
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    The subclass of Cmd
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True
    def do_EOF(self, line):
        """
        quit the program when typed
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
