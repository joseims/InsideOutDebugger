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
    try:
        ob1 = t.Object1()
        print('object ob1 was created')
        time.sleep(2)
        var1 = 3
        print('var1 was created')
        time.sleep(2)
        var2 = 'a'
        time.sleep(2)
        print('var2 was created')
        time.sleep(2)
        ob2 = t.Object2()
        print('object ob2 was created')
        time.sleep(2)
    except KeyboardInterrupt:
        d.debugger(locals(), globals(),multi_lines=True)

if (__name__ == "__main__"):
    run()

