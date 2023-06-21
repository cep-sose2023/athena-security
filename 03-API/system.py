"""
This module contains the system control functions for the application.
"""

import os
import threading
import serial
import time
from dotenv import load_dotenv

from exceptions import SystemError

ser = None
load_dotenv()
PORT = os.getenv("PORT")
BAUD_RATE = int(os.getenv("BAUD_RATE", "9600"))
lock = threading.Lock()
is_initialized = False


def setup_serial():
    """
    Sets up the serial connection using global PORT and BAUD_RATE variables.

    Description:
    The function uses the globally defined port and baud rate to establish a serial connection.
    This function does not take any arguments and does not return any values.

    Raises:
    - SystemError: If the serial connection could not be established.
    """
    global ser, is_initialized
    try:
        ser = serial.Serial(PORT, BAUD_RATE)
    except serial.SerialException:
        raise SystemError("Serial connection error")


def test_serial():
    """
    Checks if the serial connection is available and updates the global is_initialized flag.

    Description:
    The function checks if the serial connection is available by sending a test message.
    If the message is sent successfully, it sets the global flag is_initialized to True, otherwise, it sets it to False.
    This function does not take any arguments and does not return any values.
    """
    global is_initialized, ser
    with lock:
        try:
            ser.write('check'.encode())
            is_initialized = True
        except (serial.SerialException, OSError, AttributeError):
            is_initialized = False
        finally:
            time.sleep(3)


def initialize():
    """
    Initializes the system by sending 'on' command through the serial connection.

    Returns:
    - bool: True if the system was initialized successfully, False otherwise.

    Raises:
    - SystemError: If the system is already on or if there is an initialization error.

    Description:
    The function initializes the system by sending the 'on' command through the serial connection.
    If the system is already initialized, it raises a SystemError.
    """
    global is_initialized, ser
    command = 'on'
    test_serial()
    with lock:  # Acquire the lock before accessing shared variables
        try:
            if not is_initialized:
                if ser is None: setup_serial()
                ser.write(command.encode())
                ser.reset_input_buffer()
                time.sleep(1)
                is_initialized = True
                return True
            else:
                raise SystemError("System already on")
        except serial.SerialException:
            raise SystemError(f"Initialization error")
    return False


def shutdown():
    """
    Shuts down the system by sending 'off' command through the serial connection.

    Returns:
    - bool: True if the system was shut down successfully, False otherwise.

    Raises:
    - SystemError: If the system is already in standby or if there is a serial connection error.

    Description:
    The function shuts down the system by sending the 'off' command through the serial connection.
    If the system is already in standby, it raises a SystemError.
    """
    global is_initialized, ser
    command = 'off'
    test_serial()
    with lock:
        try:
            if is_initialized:
                if ser is None: setup_serial()
                ser.write(command.encode())
                ser.close()
                ser = None
                is_initialized = False
                return True
            else:
                raise SystemError("System already in standby")
        except serial.SerialException:
            raise SystemError("Serial connection error")
    return False


def restart():
    """
    Restarts the system by shutting it down first and then initializing it again.

    Returns:
    - bool: True if the system was restarted successfully, False otherwise.

    Raises:
    - SystemError: If the system is already in standby or if there is a serial connection error.

    Description:
    The function restarts the system by first shutting it down and then initializing it again.
    If the system is already in standby, it raises a SystemError.
    """
    global is_initialized
    test_serial()
    try:
        if is_initialized:
            shutdown()
            initialize()
            return True
        else:
            raise SystemError("System already in standby")
    except serial.SerialException:
        raise SystemError("Serial connection error")


def prep():
    """
    Initializes the serial connection at the beginning of the system start.

    Raises:
    - SystemError: If the serial connection could not be established.

    Description:
    The function initializes the serial connection at the beginning of the system start.
    This function does not take any arguments and does not return any values.
    """
    try:
        global ser
        ser = serial.Serial(PORT, BAUD_RATE)
        ser.write('off'.encode())
        ser.close()
        ser = None
    except serial.SerialException:
        raise SystemError("Serial connection error")
