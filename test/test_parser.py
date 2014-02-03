from rogoto import RogotoParser
from rogoto import RogotoParserException


def test_invalid_syntax():
    parser = RogotoParser()
    try:
        parser.parse('goblydegoop')
        raise AssertionError('Should have thrown a RogotoParserException')
    except RogotoParserException:
        pass

def test_pendown():
    parser = RogotoParser()
    results = parser.parse('pendown')
    assert ['pendown'] == results

def test_penup():
    parser = RogotoParser()
    results = parser.parse('penup')
    assert ['penup'] == results

def test_forward():
    parser = RogotoParser()
    results = parser.parse('forward 10')
    assert ['forward 10'] == results

def test_forward_abbreviated():
    parser = RogotoParser()
    results = parser.parse('fd 10')
    assert ['forward 10'] == results

def test_backward():
    parser = RogotoParser()
    results = parser.parse('backward 10')
    assert ['backward 10'] == results

def test_backward_abbreviated():
    parser = RogotoParser()
    results = parser.parse('bk 10')
    assert ['backward 10'] == results

def test_left():
    parser = RogotoParser()
    results = parser.parse('left 10')
    assert ['left 10'] == results

def test_left_abbreviated():
    parser = RogotoParser()
    results = parser.parse('lt 10')
    assert ['left 10'] == results

def test_right():
    parser = RogotoParser()
    results = parser.parse('right 10')
    assert ['right 10'] == results

def test_right_abbreviated():
    parser = RogotoParser()
    results = parser.parse('rt 10')
    assert ['right 10'] == results
