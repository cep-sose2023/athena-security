"""
This module contains functions to generate random numbers and
to convert them to hexadecimal form.
"""

from datetime import datetime
import os

from exceptions import GenerationError, SystemError  # Importing custom exception classes
import system  # Importing the system module
import tests  # Importing the tests module
import routes  # Importing the routes module

total_failure = False # Global variable to track total failure
PROBE_SIZE = 100 # Constant for probe size

def enforce_min_value(value, min_value):
    """
       Returns the maximum of value and min_value.

       Parameters:
       - value (int): Input value.
       - min_value (int): The minimum allowed value.

       Returns:
       - int: The maximum of value and min_value.

       Description:
       The function compares the input value with the minimum value and returns the maximum of the two.

       Example usage:
       >>> enforce_min_value(5, 10)
       10
    """
    return max(value, min_value)


def generate_binary_string(length):
    """
    Generates a binary string of given length.

    Parameters:
    - length (int): Length of the binary string to generate.

    Returns:
    - str: The generated binary string.

    Raises:
    - SystemError: If the serial connection has been cut.

    Description:
    This function generates a binary string of the given length. It does this by reading from a serial port and
    appending the binary representation of the read byte to the binary string. The function also monitors for total failure
    of the random number generator and raises an error if detected.

    Example usage:
    >>> generate_binary_string(8)
    '11010101'
    """
    global total_failure
    bytes_to_test = bytearray()
    binary_string = ""
    byte_count = 0

    try:
        while len(binary_string) < length:
            while byte_count < PROBE_SIZE:
                if system.ser.in_waiting >= 1:
                    bytes_to_test.append(int.from_bytes(system.ser.read(1), "big"))
                    byte_count += 1
            if tests.test_total_failure(bytes_to_test):
                total_failure = True
                raise GenerationError("Total failure detected.")
            for num in bytes_to_test:
                binary_string += format(num, '08b')
            byte_count = 0
            bytes_to_test = bytearray()
    except OSError as e:
        raise SystemError("The serial connection has been cut. Please check the device.") from e
    return binary_string[:length]


def binary_to_hex(binary_string):
    """
    Converts a binary string to hexadecimal form.

    Parameters:
    - binary_string (str): The binary string to convert.

    Returns:
    - str: The hexadecimal form of the binary string.

    Raises:
    - GenerationError: If a conversion error occurs.

    Description:
    This function takes a binary string as input, and converts it into its equivalent hexadecimal string. The function
    calculates the number of hexadecimal digits required based on the length of the binary string, pads the binary string
    with leading zeros if necessary, and then converts it into a hexadecimal string.

    Example usage:
    >>> binary_to_hex('01100101')
    '65'
    """
    try:
        num_bits = len(binary_string)
        num_hex_digits = -(-num_bits // 4)
        padded_binary_string = binary_string.zfill(num_hex_digits * 4)
        hex_string = hex(int(padded_binary_string, 2))[2:]
        hex_string = hex_string.zfill(num_hex_digits)
        return hex_string.upper()
    except ValueError:
        raise GenerationError("Binary to hexadecimal conversion error.")


def generate_random_numbers(count, length):
    """
    Generates random numbers in hexadecimal form.

    Parameters:
    - count (int): The number of random numbers to generate.
    - length (int): The length of each random number.

    Returns:
    - list: A list of random numbers in hexadecimal form.

    Raises:
    - GenerationError, SystemError: If an error occurs during generation of the binary string.

    Description:
    The function generates a specified count of random numbers, each of a given length. It does this by generating a
    binary string of appropriate length and then slicing it into smaller binary strings, each representing a random
    number. These binary strings are then converted into hexadecimal form.

    Example usage:
    >>> generate_random_numbers(2, 8)
    ['1F', '2B']
    """
    global total_failure
    total_failure = False
    hex_strings = []
    try:
        binary_string = generate_binary_string(count * length)
    except (GenerationError, SystemError) as e:
        print(f"Error occurred while generating random numbers: {str(e)}")
        return None
    if total_failure:
        slicing_steps = len(binary_string) // length
    else:
        slicing_steps = count
    counter = 1
    slicing_steps += 1
    start_idx = 0
    while counter < slicing_steps:
        end_idx = counter * length
        hex_strings.append(binary_to_hex(binary_string[start_idx:end_idx]))
        start_idx = end_idx
        counter += 1
    return hex_strings


def generate_random_numbers_to_file(length: int, filetype: str) -> bool:
    """
    Generates a binary string of random numbers and writes it to a file.

    Parameters:
    - length (int): The number of random numbers to generate.
    - filetype (str): The type of file to write to. Should be 'txt' or 'bin'.

    Returns:
    - bool: True if successful, False otherwise.

    Raises:
    - IOError: If an error occurs while writing to the file.

    Description:
    This function generates a binary string of random numbers and writes it to a file. It first generates a binary string
    of random numbers. Then, based on the filetype specified, it either writes the binary string directly to a text file,
    or converts it into bytes and writes it to a binary file.

    Example usage:
    >>> generate_random_numbers_to_file(8, 'txt')
    True
    """
    now = f"{datetime.now().strftime('%Y-%m-%d_%H-%M')}"
    filename = f"{now}.{filetype}"
    routes.filepath = os.path.join(os.getcwd(), filename)
    try:
        binary_string = generate_binary_string(length)
    except GenerationError as e:
        print(f"Error occurred while generating random numbers to file: {str(e)}")
        return False
    try:
        if filetype == 'txt':
            with open(routes.filepath, 'w') as f:
                f.write(binary_string)
        elif filetype == 'bin':
            with open(routes.filepath, 'wb') as f:
                f.write(int(binary_string, 2).to_bytes((length + 7) // 8, byteorder='big'))
        return True
    except IOError as e:
        print(f"IOError occurred while writing to file: {str(e)}")
        return False