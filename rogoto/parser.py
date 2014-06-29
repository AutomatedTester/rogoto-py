import re


class RogotoParser(object):
    """Parse Rogoto Commands"""
    def __init__(self):
        """
            When creating a new class it will initialise with an empty
            array of code to execute and the pen state to be up.
        """
        self.code_to_execute = []
        self.pen_state = 'up'

    def parse(self, commands):
        """
            Parses a string to find the Rogoto commands and returns an array of the
            commands.

            :param commands:
                commands (str): A string of commands that are seperated by a \\\\n character

            Return list
                 A list of the commands that have been parsed so that they can be executed
                 by iterating over the list

        """
        cmdRegex = r'pendown|pd|penup|pu|forward \d+|fd \d+|backward \d+|bk \d+|left \d+|lt \d+|right \d+|rt \d+'
        cmd = commands.split('\n')
        for x in range(len(cmd)):
            matches = re.search(cmdRegex, cmd[x])
            if matches is None:
                raise RogotoParserException('Invalid Syntax was found')
            else:
                if 'fd' in matches.group(0):
                    self.code_to_execute.append(matches.group(0).replace('fd', 'forward'))
                elif 'bk' in matches.group(0):
                    self.code_to_execute.append(matches.group(0).replace('bk', 'backward'))
                elif 'lt' in matches.group(0):
                    self.code_to_execute.append(matches.group(0).replace('lt', 'left'))
                elif 'rt' in matches.group(0):
                    self.code_to_execute.append(matches.group(0).replace('rt', 'right'))
                elif 'pd' in matches.group(0):
                    self.code_to_execute.append('pendown')
                    self.pen_state = 'down'
                elif 'pu' in matches.group(0):
                    self.code_to_execute.append('penup')
                    self.pen_state = 'up'
                else:
                    self.code_to_execute.append(matches.group(0))
                    if matches.group(0) == 'penup':
                        self.pen_state = 'up'
                    elif matches.group(0) == 'pendown':
                        self.pen_state = 'pendown'

        return self.code_to_execute

    def clear(self):
        """
            Clears the code that will be executed
        """
        self.code_to_execute = []


class RogotoParserException(Exception):
    """Exception object when there is invalid items in the code """
    def __init__(self, message):
        self.message = message
