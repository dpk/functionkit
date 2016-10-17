from collections import deque

import pytest

from functionkit.strict import *


@pytest.fixture
def integers_fn():
    def f():
        yield 1
        yield 2
        yield 3

    return f


def test_strictify(integers_fn):
    integers_fn = strictify(deque)(integers_fn)
    assert integers_fn() == deque([1, 2, 3])

def test_listify(integers_fn):
    integers_fn = listify(integers_fn)
    assert integers_fn() == [1, 2, 3]

def test_setify(integers_fn):
    integers_fn = setify(integers_fn)
    assert integers_fn() == set([1, 2, 3])

def test_dictify():
    @dictify
    def integers_letters_fn():
        yield ('a', 1)
        yield ('b', 2)
        yield ('c', 3)

    assert integers_letters_fn() == {'a': 1, 'b': 2, 'c': 3}
