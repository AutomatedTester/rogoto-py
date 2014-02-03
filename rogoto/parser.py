import re


class RogotoParser(object):
    """Parse Rogoto Commands"""
    def __init__(self):
        self.code_to_execute = []

    def parse(self, commands):
        cmdRegex = r'pendown|penup|forward \d+|fd \d+'
        matches = re.search(cmdRegex, commands)
        if matches is None:
            raise RogotoParserException('Invalid Syntax was found')
        else:
            if 'fd' in matches.group(0):
                self.code_to_execute.append(matches.group(0).replace('fd', 'forward'))
            else:
                self.code_to_execute.append(matches.group(0))

        return self.code_to_execute


class RogotoParserException(Exception):
    """Exception object when there is invalid items in the code """
    def __init__(self, message):
        self.message = message
