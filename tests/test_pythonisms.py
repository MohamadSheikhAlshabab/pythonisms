from pythonisms import __version__ 
from pythonisms.pythonisms import LinkedList , Node
from pythonisms.decorators.decorators import slow_down ,spent
import time
import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_len():
    list1= LinkedList()
    list1.insert(12)
    list1.insert(5)
    list1.insert(7)
    list1.insert(99)
    actual = len(list1)
    expected = 4
    assert actual == expected

def test_str():
    list1= LinkedList()
    list1.insert(12)
    list1.insert(5)
    list1.insert(7)
    list1.insert(99)
    actual = list1.__str__()
    expected = "[ 12 ] -> [ 5 ] -> [ 7 ] -> [ 99 ] -> None"
    assert actual == expected

def test_getitem():
    list1= LinkedList()
    list1.insert(12)
    list1.insert(5)
    list1.insert(7)
    list1.insert(99)
    actual = list1.__getitem__(2)
    expected = 7
    assert actual == expected

def test_eq():
    list1= LinkedList()
    list1.insert(12)
    list1.insert(5)
    list1.insert(7)
    list1.insert(99)
    actual = list1.__eq__(list1)
    expected = True
    assert actual == expected
