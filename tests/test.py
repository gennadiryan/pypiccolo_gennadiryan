import numpy as np

from pypiccolo_gennadiryan import hello
from pypiccolo_gennadiryan import utils

def test_hello():
    assert hello.hello() == 'Hello, world!'

def test_random_array():
    for shape in [(3,), (2, 2,), (1, 1, 1,)]:
        assert utils.random_array(shape).shape == shape
