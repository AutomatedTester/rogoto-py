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
