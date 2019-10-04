import traceback
import sys
import readline


def debugger(locals_, globals_, multi_lines=False, input_history=True,
             safe_word="continue"):
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
    """
    locals_.update({"EXCEPTION": "No exception yet"})
    __input_history(input_history)

    input_func = __get_input_func(multi_lines)

    print("\nSTARTING DEBUG")
    while True:
        cmd = input_func()

        if (cmd == safe_word):
            break

        __exec_command(cmd, globals_, locals_, safe_word)

    print("QUITTING DEBUG")


def __exec_command(cmd, globals_, locals_, safe_word):
    try:
        exec(cmd, globals_, locals_)
    except Exception as e:
        print("SOMETHING WENT WRONG")
        print(traceback.format_exc())
        locals_.update({"EXCEPTION": e})


def __get_input_func(multi_lines):
    if (multi_lines):
        return sys.stdin.readlines
    return input


def __input_history(input_history):
    if input_history:
        readline.set_auto_history(True)
