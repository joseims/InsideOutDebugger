import debugger as d
class Test1():
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def fun_test(self):
        print(self.a,self.b)

class Test2():
    def __init__(self):
        self.a = 'c'
        self.b = 'd'
        d.debuger(locals_=locals())

    
    def fun_test(self):
        print(self.a,self.b)