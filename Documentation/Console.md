Each task here will help with the flow

1. Put in place a parent class(BaseModel) to take care of initialization, serialization and desearilazation of future instances
1. create a simple flow of serialiaion and deserialization:
```
Instance <---> Dictionary <----> JSON string <---> file.json
```
1. Create all classes used for the AirBnB: They all inherit from the BaseModel
	- User
	- State
	- City
	- Place
1. Create the first abstracted storage engine for the project. File storage
1. Create all unittest to validate all our classes and storage engine

We want to create a console that will be able to di the following
1. Create a new object( such as a new User or a new Place)
1. Retrieve an object from a file or a database
1. Do a number of operations on the object(count, compute stats, etc)
1. Destroy an object

This will show us how to come up with  console that we will use to perform varous administrative tasks on our airbnb clone

## cmd module.
We can use this module to give our python program a shell interface. It is often useful for administrative tools, protoypes and test harnessnesthat will later be wrapped in amore sophisticated interface.

This module defines only one class the **Cmd** class to be used as a base class for command processors such interactive shells and other command interpreters. 
By default it uses readline for interactive prompt handling, commandline editing and command completion

### What is readline?
This is a module that is used to enhance interactive command line arguments to make them easier to use. It provides 'tab completion'

## Processing of commands
The interpreter uses a loop to:
 - read all lines from its input
 - parse them
 - dispartch the command to the appropriate command handler

The input lines are parsed into two parts:
1. the command
1. any other text on the line

Example if I enter a command "foo bar" and my class includes a method named *do_foo()* , then the method is called with *bar* as the argument.

The marker to the EOF(end-of-file) is is sent to the *do_EOF()* if a command handler returns true value, the program will exit cleanly.

The following below is a small example that support the greet command. so when you type "greet" on the command line you get a response saying hello
```
import cmd

class Hello(cmd.Cmd):
	def do_greet(self, line):
		print("hello")
	
	def do_EOF(self, line):
		return True
if __name__ == '__main__':
	Hello().cmdloop()
```

When we run the file containing the code above
```
python3 file.py
```
The first thing we will notice is the *(Cmd)* prompt. If you want to configure this prompt to show something of your liking you can use the attribute *prompt* 

if I use the greet command, i.e 
```
(Cmd) greet
```
do_greet() method is invoked to handle it. in turn it prints "hello"

If maybe you have entered a command whose method you have not specified, the default() method is called with the entire input line as an argument. It then reports an error.

```
(Cmd) foo
*** Unknown syntax: foo
(Cmd) 
```
Since do_EOF returns True, if we type Ctrl+D we will exit the interpreter

The following below is a better version of what we did earlier

```
import cmd

class Hello(cmd.Cmd):
	""" simple command processor"""
	
	def do_greet(self, person):
		""" greet [person]"""
		if person:
			print("hi, ".format(person))
		else:
			print('hi there')
	def do_EOF(self, line):
		return True
	
	def postloop(self):
		print

if __name__ == '__main__':
	Hello().cmdloop()
```
When you type help you get the following response:

```
(Cmd) help

Documented commands (type help <topic>):
========================================
greet  help

Undocumented commands:
======================
EOF

(Cmd)
```
and then when you type
```
(Cmd) help greet
 greet [person]
(Cmd)
```
The docstring that you added in the method do_greet() becomes the help text for the command

## The help Handler
an alternative solution to get a better help message more good looking for *greet* command we can implement help_greet() method. when this method is available, the help handler is called on to produce help text for the named command.

```
import cmd

class Hello(cmd.Cmd):
    """simpe command processor"""

    def do_greet(self, person):
        if person:
            print("hi, {}".format(person))
        else:
            print("hi")

    def help_greet(self):
        print ('\n'.join([ 'greet [person]',
                            'Greet the named person']))

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    Hello().cmdloop()
```
```
(Cmd) help greet
greet [person]
Greet the named person
```
it is now upto the help handler to actually ouptput the help message

## Auto Completion

Cmd also includes support for command completion. the user will trigger completion by hitting the tab key at an input prompt.
once the command is known, argument completion is handled by methods with a prefix *complete__* It will allow you to assemble a list of possible completions using your own criteria:
 - maybe query a database
 - look at a file or dir on the filesystem.
In our case we have hard coded a set of "friends" . A real program would probably save the list somewhere and either read it once and cashe the contents to be scanned as needed.
 

```
import cmd

class Hello(cmd.Cmd):
    """simpe command processor"""

    FRIENDS = [ 'Hassan', 'Hamisi', 'Hansel', 'Barbra', 'Bob' ]

    def do_greet(self, person):
        """ greet the person """
        if person and person in self.FRIENDS:
            print("hi, {}".format(person))
        elif person:
            print("hi, ".format(person))
        else:
            print("hi")

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [f
                            for f in self.FRIENDS
                            if f.startswith(text)
                            ]
        return completions

    def help_greet(self):
        print ('\n'.join([ 'greet [person]',
                            'Greet the named person']))

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    Hello().cmdloop()
```
```
(Cmd) greet
greet
(Cmd) greet Ha
Hamisi  Hansel  Hassan  
(Cmd) greet Hassan
hi, Hassan
(Cmd) greet Hassan
hi, Hassan
```

## Configuring Cmd Through Attributes

 *prompt* can be used to set a string to be printed each time the user is asked for a new command

**intro** is the "welcome" message printed at the start of the program.

Any command that returns a True value stops the interpreter

for more information on this module I have provided a link below that will offer you the required support

[Console module](https://wiki.python.org/moin/CmdModule)
