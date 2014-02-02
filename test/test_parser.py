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
