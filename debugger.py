import traceback
import sys
import platform

class Debugger():

    def __init__(self, locals_, globals_, multi_lines=False, input_history=True):
        """
        Summary line.

        Extended description of function.

        Parameters
        ----------
        locals : set
            The set of local variables at the state where you want to debug
        globals : set
            The set of global variables at the state you want to debug
        multi_lines: boolean
            If this is enabled you will be able to write multi-lines code.
            Works better for writting functions(Default false)
        input_history: boolean
            Wheter you want it or not to be able to use previews
            commands with up arrow(Default true)
        safe_word: string
            The string that is used to pass the debugger and
            continue with the program flow
        Returns
        -------
        None
            It does not return
        """
        self.locals_ = locals_
        self.globals_ = globals_
        self.multi_lines = multi_lines

        if platform.system() != 'Windows':
            readline = __import__('readline')
            self.input_history = input_history
        else:
            self.input_history = False

        self.safe_word = "continue"

    def debug(self):

        self.locals_.update({"EXCEPTION": "No exception yet"})
        self.__input_history()

        input_func = self.__get_input_func()

        print("\nSTARTING DEBUG")
        while True:
            cmd = input_func()

            if (cmd == self.safe_word):
                break

            self.__exec_command(cmd)

        print("QUITTING DEBUG")


    def __exec_command(self, cmd):
        try:
            exec(cmd, self.globals_, self.locals_)
        except Exception as e:
            print("SOMETHING WENT WRONG")
            print(traceback.format_exc())
            locals_.update({"EXCEPTION": e})


    def __get_input_func(self):
        if self.multi_lines:
            return sys.stdin.readlines
        return input


    def __input_history(self):
        if self.input_history:
            readline.set_auto_history(True)
