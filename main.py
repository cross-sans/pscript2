import cmd
import subprocess
import compiler
import importlib
import sys
import json

class Comand(cmd.Cmd):
    try:
        with open("usr.json",'r') as t:
            dat = json.load(t)
        user = dat["name"]
        password = dat["p"]
    except:
        username = input("your name ")
        password = input("your password ")
        dat = {"name":username, "p":password}
        with open("usr.json",'w') as t:
            json.dump(dat,t)
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
    def do_config(self):
        """
        changes you user credentials
        """
        username = input("your name ")
        password = input("your password ")
        dat = {"name":username, "p":password}
        with open("usr.json",'w') as t:
            json.dump(dat,t)

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

    def do_quit(self):
        """
        quits app
        """
        return True


if __name__ == '__main__':
    command = Comand()
    command.cmdloop()