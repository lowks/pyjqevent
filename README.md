A jquery-like event system for python

```python
import jqevent

def hello():
    print "hello"

e = jqevent.Eventful()

e.on('hi', hello)

e.trigger('hi')
```


Currently supports:
* on
* off
* one
* trigger
