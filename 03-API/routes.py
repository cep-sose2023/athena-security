"""
This module defines the Flask API routes for the application.
"""
from flask import jsonify, send_file, request, Flask
from flask_cors import CORS

# Importing exception and system modules
import exceptions
import system

# Importing required functions and classes from these modules
from exceptions import GenerationError
from system import initialize, shutdown, restart
from generation import enforce_min_value, generate_random_numbers, generate_random_numbers_to_file

# Initialize Flask app
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for all origins on routes beginning with '/trng/*'
CORS(app, resources={r"/trng/*": {"origins": "*"}})

# Declare a variable to store file paths
filepath = ""


@app.route('/trng/randomNum/init', methods=['GET'])
def init_random_number_generator():
    """
    Initializes the random number generator system

    Returns:
        A  JSON response indicating whether initialization was successful or
        an error occurred.
    """
    try:
        # Check if initialization is successful
        if initialize():
            return jsonify({'message': 'System initialised successfully'}), 200
        else:
            return jsonify({'message': 'System already initialized'}), 409
    except exceptions.SystemError as e:
        # If there is a SystemError, return the error message with a custom status code 555
        return jsonify({'error': str(e)}), 555


@app.route('/trng/randomNum/getRandom', methods=['GET'])
def get_random_numbers():
    """
    Generates and returns a set of random numbers.

    Returns:
        A JSON response with the generated random numbers or an error message.
    """
    try:
        system.test_serial()
        if not system.is_initialized:
            return jsonify({'message': 'System not initialized'}), 432

        # Get the number of bits and quantity from request arguments, default to 1 if not provided
        length = enforce_min_value(request.args.get('numBits', default=1, type=int), 1)
        count = enforce_min_value(request.args.get('quantity', default=1, type=int), 1)

        # Generate the random numbers
        random_numbers = generate_random_numbers(count, length)

        # Return the generated random numbers
        return jsonify(random_numbers), 200
    except (GenerationError, exceptions.SystemError) as e:
        # If there is a GenerationError or SystemError, return the error message with a custom status code 555
        return jsonify({'error': str(e)}), 555


@app.route('/trng/randomNum/generateTestdata', methods=['GET'])
def get_testdata():
    """
    Generates a set of test data.

    Returns:
        A JSON response indicating whether test data generation was successful
        or an error occurred.
    """
    try:
        system.test_serial()
        if not system.is_initialized:
            return jsonify({'message': 'System not initialized'}), 432

        # Get the number of bits and file type from request arguments
        length = enforce_min_value(request.args.get('numBits', default=5000, type=int), 1)
        filetype = request.args.get('filetype', default='bin')

        # Generate random numbers and write them to a file
        if generate_random_numbers_to_file(length, filetype):
            return jsonify({'message': 'Generation successful'}), 200
        else:
            return jsonify({'message: Generation failed'}), 555
    except GenerationError as e:
        # If there is a GenerationError, return the error message with a custom status code 555
        return jsonify({'error': str(e)}), 555


@app.route('/trng/randomNum/downloadFile', methods=['GET'])
def download():
    """
    Allows downloading a file.

    Returns:
        The requested file for download, or a Flask JSON response with an error
        message if the file could not be found.
    """
    try:
        # Return the requested file for download
        return send_file(filepath, as_attachment=True), 200
    except FileNotFoundError as e:
        # If the file was not found, return a JSON response with the error message and a custom status code 555
        return jsonify({'error':  str(e)}), 555


@app.route('/trng/randomNum/shutdown', methods=['GET'])
def shutdown_random_number_generator():
    """
    Puts the random number generator system in standby mode.

    Returns:
        A JSON response indicating whether shutdown was successful or
        an error occurred.
    """
    try:
        # Check if the shutdown process was successful
        if shutdown():
            return jsonify({'message': 'System successfully shutdown'}), 200
        else:
            return jsonify({'message': 'System already in standby'}), 200
    except exceptions.SystemError as e:
        # If there is a SystemError, return the error message with a custom status code 555
        return jsonify({'error': str(e)}), 555


@app.route('/trng/randomNum/restart', methods=['GET'])
def restart_random_number_generator():
    """
    Restarts the random number generator system.

    Returns:
        A JSON response indicating whether restart was successful or
        an error occurred.
    """
    try:
        # Check if the restart process was successful
        if restart():
            return jsonify({'message': 'System successfully restarted'}), 200
        else:
            return jsonify({'message': 'System already in standby'}), 200
    except exceptions.SystemError as e:
        # If there is a SystemError, return the error message with a custom status code 555
        return jsonify({'error': str(e)}), 555


@app.errorhandler(404)
def page_not_found(e):
    """
    Handles the 404 error when the requested page is not found.

    Returns:
    - A JSON response indicating the error message and the HTTP status code 404.
    """
    return jsonify({'error': str(e)}), 404
