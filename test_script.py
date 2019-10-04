import test_class as t
import debugger as d
import time

'''
This is a test file, so you can understand how to use the debbuger
you can trigger the keyboard Interrupt by pressint CTRL+C at any time
during the execution.

This will give you acess to all the variable's that exist at the runtime

'''


def run():
    test1 = t.Test1()
    print('object test1 was created')
    time.sleep(2)
    variable1 = 3
    print('variable1 was created')
    time.sleep(2)
    variable2 = 'a'
    time.sleep(2)
    print('variable2 was created')
    time.sleep(2)
    b = t.Test2()
    print('object test2 was created')
    time.sleep(2)


if (__name__ == "__main__"):
    try:
        run()
    except KeyboardInterrupt:
        d.debugger(locals(), globals())
