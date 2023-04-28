import cmd
import subprocess
import compiler
import importlib
import sys
import imp


class Comand(cmd.Cmd):
    user = "test"
    print("type ? or help for commands")
    prompt = f"{user}> "

    def do_pscript(self, arg):
        """
        compiles a pscript file to python then executes it
        """
        compiler.compile_pscript(arg)

    def do_neo(self, arg):
        """
        compiles a neo file into python, then executes it
        """
        compiler.compile_neo(arg)


    def do_reload(self, arg):
        """
        Reloads the current module.
        """
        module = imp.reload(sys.modules[__name__])
        print(f"{module.__name__} module reloaded")



    def do_run(self, arg):
        """
        runs the file you give it
        """
        subprocess.run(['python', arg])


if __name__ == '__main__':
    command = Comand()
    command.cmdloop()