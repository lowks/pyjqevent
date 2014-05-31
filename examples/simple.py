#!/usr/bin/env python

import jqevent


def hello():
    print "Hello"


def what():
    print "What?"

e = jqevent.Eventful()
e.on('hi', hello)
e.on('hi', what)

e.trigger('hi')
