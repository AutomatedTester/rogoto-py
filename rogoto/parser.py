import re


class RogotoParser(object):
    """Parse Rogoto Commands"""
    def __init__(self):
        pass

    def parse(self, commands):
        cmdRegex = r'pendown'
        matches = re.search(cmdRegex, commands)
        if matches is None:
            raise RogotoParserException('Invalid Syntax was found')


class RogotoParserException(Exception):
    """Exception object when there is invalid items in the code """
    def __init__(self, message):
        self.message = message
