import traceback
import sys
import readline



def debuger(locals_=locals(), globals_=globals() , exec_=0, printer = 1, multi_lines = 0, input_history=1, safe_word="continue"):

    __input_history(input_history)

    eval_fun = __get_eval_fun(exec_,printer)
    input_fun = __get_input_fun(multi_lines,exec_)
    
    print("STARTING DEBUG")
    while True:
        cmd = input_fun()
        __exec_command(cmd, globals_, locals_, safe_word)
        
    print("QUITTING DEBUG")

def __exec_command(cmd,globals_,locals_,safe_word):
    try:
        if (cmd == safe_word): break
        eval_fun(cmd, globals_, locals_)
    except Exception:
        print("SOMETHING WENT WRONG")
        print(traceback.format_exc())


def __get_eval_fun(exec_, printer):
    if exec_:
        return exec

    def eval_wrap(input,*args):
        ret = eval(input,*args)
        print(ret)

    if printer:
        return eval_wrap

    return eval

def __get_input_fun(multi_lines, exec_):
    if (multi_lines and exec_):
        return sys.stdin.readlines
    
    return input

def __input_history(input_history):
    if input_history:
        readline.set_auto_history(True)