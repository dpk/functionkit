# functionkit

A potpourri of functional programming tools for Python 3. Not much here right now, but there will be soon I hope!

## `functionkit.strict`

When you want to make a lazy generator in Python, it's easy:

```python
def fizzbuzz(input):
    for n in input:
        if n % 3 == 0 and n % 5 == 0:
            yield 'fizzbuzz'
        elif n % 3 == 0:
            yield 'fizz'
        elif n % 5 == 0:
            yield 'buzz'
        else:
            yield n
```

but if you want to make the function return a strict list that can be indexed immediately, or just passed to another function like `reversed` that can't deal with lazy iterators, you typically have to transform it completely to something like this:

```python
def fizzbuzz(input):
    result = []
    for n in input:
        if n % 3 == 0 and n % 5 == 0:
            result.append('fizzbuzz')
        elif n % 3 == 0:
            result.append('fizz')
        elif n % 5 == 0:
            result.append('buzz')
        else:
            result.append(n)
    
    return result
```

i.e. explicitly mutating the list. This is not very nice.

`functionkit.strict` provides the decorators `listify`, `setify`, and `dictify` which convert the values from a generator to a `list`, `set`, or `dict` respectively. These are all based on the more primitive `strictify` so you can produce results of any kind, like a `collection.deque` for fast appends to either end of the result list.

```python
@listify
def one_two_three():
    yield 1
    yield 2
    yield 3

one_two_three() #=> [1, 2, 3]

@dictify
def animals():
    # yield two-tuples
    yield ('tiger', 'panthera tigris')
    yield ('kiwi', 'apteryx haastii')
    yield ('goldfish', 'carassius auratus')

animals() #=> {'tiger': 'panthera tigris', 'kiwi': 'apteryx haastii', 'goldfish': 'carassius auratus'}

@strictify(collections.deque)
def planets():
    yield 'earth'
    yield 'mars'
    yield 'jupiter'

solar_system = planets()
solar_system.append('uranus')
solar_system.appendleft('venus')
solar_system #=> deque(['venus', 'earth', 'mars', 'jupiter', 'uranus'])
```

Note these will all diverge and run out of memory if you generate an infinite stream with them!
