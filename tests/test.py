import pytest

import pypiccolo_gennadiryan.hello as super_hello
import pypiccolo_gennadiryan.sub_hello.hello as sub_hello
import pypiccolo_gennadiryan.math as math

def test_super_hello():
    assert super_hello() == 'Hello, universe!'

def test_sub_hello():
    assert sub_hello() == 'Hello, world!'

def test_random_array():
    for shape in [(3,), (2, 2,), (1, 1, 1,)]:
        assert math.random_array(shape).shape == shape
