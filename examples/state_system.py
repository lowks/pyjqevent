#!/usr/bin/env python

import jqevent


class StateSystem(jqevent.Eventful):
    def __init__(self):
        jqevent.Eventful.__init__(self)
        self.on('a', self.a)
        self.on('b', self.b)
        self.on('c', self.c)
        self.b_visits = 0

    def a(self):
        print("In {}.a".format(self))
        self.trigger('b')

    def b(self):
        print("In {}.b".format(self))
        self.b_visits += 1
        print("\tb was visited {} times".format(self.b_visits))
        if self.b_visits < 3:
            self.trigger('a')
        else:
            self.trigger('c')

    def c(self):
        print("In {}.c".format(self))
        print("Reached the end!")

    def start(self):
        print("Triggering start state(a)")
        self.trigger('a')


ss = StateSystem()
ss.start()
