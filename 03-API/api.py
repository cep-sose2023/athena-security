"""
Main entry point for the application.
"""

import system
from routes import app

if __name__ == '__main__':
    try:
        # Initialize the system before running the app
        system.prep()
        # Run the Flask application
        app.run()
    except Exception as e:
        print(f"An error occurred while running the application: {str(e)}")
