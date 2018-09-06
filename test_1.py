import pytest

from arquivo import soma, menos, this_num


def test_mais():
        assert soma(3,2) == 5
        assert soma(3,3) == 6
        assert soma(2.5,  1.5) == 4
        assert soma( -3, -11) == -14


def test_usandostring():
        assert soma('3', '5') == 8
        assert soma('xyz',1) == None

def test_menos():      
        assert menos(3,3) == 0
