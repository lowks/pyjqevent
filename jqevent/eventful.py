#!/usr/bin/env python

from collections import defaultdict


class Function(object):
    def __init__(self, function, *args, **kwargs):
        """
        Save the args and kwargs for this function
        """
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        """
        if args or kwargs are undefined (None), the
        saved args and kwargs are used
        """
        a = self.args if len(args) == 0 else args
        k = self.kwargs if len(kwargs) == 0 else kwargs
        return self.function(*a, **k)


class Eventful(object):
    """
    An object that emits and handles jquery like events
    """
    def __init__(self):
        self.handlers = defaultdict(dict)
        self._id = 0
        self._ones = []

    def on(self, key, function, *args, **kwargs):
        if not isinstance(function, Function):
            function = Function(function, *args, **kwargs)
        cbid = self._id
        self._id += 1
        self.handlers[key][cbid] = function
        return cbid

    def off(self, key=None, function=None):
        if key is not None:
            if function is None:
                if key not in self.handlers:
                    raise Exception  # TODO description
                self.handlers[key] = {}
                return
            search_space = {key: self.handlers[key]}
        else:
            search_space = self.handlers
        if function is not None:  # key is also None
            if isinstance(function, int):
                ft = lambda k, f: k == function
            elif isinstance(function, Function):
                ft = lambda k, f: f == function
            else:  # assumes this is a function
                ft = lambda k, f: f.function == function
            for key in search_space.keys():
                for cbid in search_space[key].keys():
                    if ft(cbid, search_space[key][cbid]):
                        del self.handlers[key][cbid]
                        return
            # if this point is reached, the function was not found
            raise Exception  # TODO description
        self.handlers = defaultdict(dict)  # if both None, remove all

    def one(self, key, function, *args, **kwargs):
        cbid = self.on(key, function, *args, **kwargs)
        self._ones.append(cbid)
        return cbid

    def trigger(self, key, *args, **kwargs):
        results = {}
        for cbid in self.handlers[key].keys():
            results[cbid] = self.handlers[key][cbid](*args, **kwargs)
            if cbid in self._ones:
                del self.handlers[key][cbid]
                self._ones.remove(cbid)
        return results


class Signal(Eventful):
    def __init__(self):
        pass

    def connect(self, f):
        pass

    def disconnect(self, f):
        pass

    def emit(self, *args, **kwargs):
        pass
