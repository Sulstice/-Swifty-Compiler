# -*- coding: utf-8 -*-
from yacc import yacc
import cmd

class MiniLisp(cmd.Cmd):     # See https://docs.python.org/2/library/cmd.html

    env = {}

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">>> "
        self.intro  = "Welcome to Swifty"

    def do_exit(self, args):
        """Exits from the console"""
        return -1

    def do_EOF(self, args):
        """Exit on system end of file character"""
        print ("Good bye!")
        return self.do_exit(args)

    def do_help(self, args):
        print (self.__doc__)

    def emptyline(self):    
        """Do nothing on empty input line"""
        pass

    def default(self, line):       
        """Called on an input line when the command prefix is not recognized.
           In that case we execute the line as Python code."""
        ast = yacc.parse(line)
        print ('AST:', ast)
        import lis
        print ('RESULT:', lis.eval(ast))

if __name__ == '__main__':
        ml = MiniLisp()
        ml.cmdloop()     # See https://docs.python.org/2/library/cmd.html
