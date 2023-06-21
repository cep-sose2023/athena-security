"""
Module defining custom exceptions for this application.
"""


class GenerationError(Exception):
    """
    Exception raised for errors encountered during random number generation.

    Attributes:
    - message (str): Explanation of the error.

    Description:
    This class is used to create a custom exception, named GenerationError, which can be raised whenever there's an error
    during random number generation in this application. It inherits from the built-in Exception class.
    The constructor of this class takes a message as an argument, which is a string that explains the error.
    """
    def __init__(self, message):
        self.message = message


class SystemError(Exception):
    """
    Exception raised for system-level errors, like issues with the serial connection.

    Attributes:
    - message (str): Explanation of the error.

    Description:
    This class is used to create a custom exception, named SystemError, which can be raised whenever there's a system-level
    error, like an issue with the serial connection in this application. It inherits from the built-in Exception class.
    The constructor of this class takes a message as an argument, which is a string that explains the error.
    """
    def __init__(self, message):
        self.message = message
