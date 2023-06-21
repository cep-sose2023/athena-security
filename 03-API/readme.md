# Backend: Python Flask API

This is a Python Flask API that supports the Athena-Security True Random Number Generator (TRNG) frontend single-page application. The API provides system control, generates random numbers, and supports file downloads.



## 🖨️ Technologies Used

This part of the TRNG is a Backend API built using:

- Python3: A high-level, interpreted programming language used to create the backend service.
- Flask: A micro web framework written in Python.
- Flask-RESTful: An extension for Flask that adds support for quickly building REST APIs.
- Numpy: A library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
- Pandas: A software library written for data manipulation and analysis.



## ⭐ Features

The True Random Number Generator (TRNG) backend API offers robust, efficient support for the frontend application and includes the following features:

1. 🖥️ System Control
   - Shutdown the system
   - Restart the system
2. 🔢 Generate Random Numbers
   - Generate random numbers based on the provided parameters (number of bits and quantity)
3. 💾 Download Files
   - Generate downloadable files of random numbers by specifying the number of bits and file type (binary or text)
   - Sends the generated file for download in the frontend.



## 🔌 Endpoints

### Main Endpoint

##### `GET /trng/randomNum/getRandom`

This endpoint returns an array of sequences of bits of a specified length and quantity. The API guarantees that the sequences are randomly drawn. The length and quantity of the sequences can be specified using the following query parameters:

- numBits (optional, integer, minimum 1, default 1): The number of random bits in each bit sequence.
- quantity (optional, integer, minimum 1, default 1): The number of random sequences to generate.

**Responses**

- **200 OK**: The response is an array of strings, where each string is a randomly generated bit sequence of the specified length. The bit sequences are encoded as hexadecimal strings, with leading zeros if necessary. Example response:

  ```css
  [     "08c1f27b",     "12d45f38",     "9a6b7c5d"]
  ```

- **503 Service Unavailable**: This error code is returned if the system is not ready to generate random numbers, such as when the random number source is in standby mode or is not reachable.

- **555 Internal Server Error**: This error code is returned if the system is unable to initialize within 60 seconds.

**Example Usage**

To generate 10 random bit sequences of length 8 using curl, you can run the following command:

```bash
curl "https://172.16.78.59:8443/trng/randomNum/getRandom?numBits=8&quantity=10"
```



### System Control

##### `GET /trng/randomNum/init`

This endpoint initializes the random number generator. If the system is already initialized, a message indicating this fact will be returned.

**Responses:**

- **200 OK**: The system was initialized successfully. Example response: `{'message': 'System initialised successfully'}`
- **409 Conflict**: The system is already initialized. Example response: `{'message': 'System already initialized'}`
- **555 Internal Server Error**: There was an error during system initialization.

**Example Usage:**

```bash
curl "https://172.16.78.59:8443/trng/randomNum/init"
```



##### `GET /trng/randomNum/shutdown`

This endpoint shuts down the random number generator. If the system is already in standby, a message indicating this fact will be returned.

**Responses:**

- **200 OK:** The system was shutdown successfully. Example response: `{'message': 'System successfully shutdown'}`
- **409 Conflict**: The system is already shut down. Example response: `{'message': 'System already shut down'}`
- **555 Internal Server Error**: There was an error during system shutdown.

**Example Usage:** 

```bash
curl "https://172.16.78.59:8443/trng/randomNum/shutdown"
```



### Additional Endpoints

##### `GET /trng/randomNum/generateTestdata`

This endpoint generates a set of test data. The length and type of the data can be specified using the following query parameters:

- numBits (optional, integer, minimum 1, default 5000): The length of the data to generate.
- filetype (optional, string, default 'bin'): The type of the file to generate.

**Responses:**

- **200 OK**: The data was generated successfully. Example response: `{'message': 'Generation successful'}`
- **432 Service Unavailable**: The system is not ready to generate test data.
- **555 Internal Server Error:** There was an error during data generation.

**Example Usage:**

```bash
curl "https://172.16.78.59:8443/trng/randomNum/generateTestdata?numBits=1000&filetype=txt"
```



##### `GET /trng/randomNum/downloadFile`

After calling the `/trng/randomNum/generateTestdata` endpoint, you can use this endpoint to download a file that contains a set of test data.

**Responses:**

- **200 OK**: The file download begins.
- **555 Internal Server Error**: The requested file could not be found or there was an error during the file download.

**Example Usage**: 

```bash
curl "https://172.16.78.59:8443/trng/randomNum/downloadFile"
```



##### `GET /trng/randomNum/restart`

This endpoint restarts the random number generator. If the system is already in standby, a message indicating this fact will be returned.

**Responses:**

- **200 OK**: The system was restarted successfully. Example response: `{'message': 'System successfully restarted'}`
- **555 Internal Server Error**: There was an error during system restart.

**Example Usage**:

```bash
curl "http://localhost:5000/trng/randomNum/restart"
```



Please note that for each of these endpoints, the 555 error code is returned for any exceptions not explicitly caught by the system, indicating an unexpected server error.



## 🛠️ Installation

To install the application and its dependencies, make sure you have Python installed. Python is used to run the application server and build the backend service. Install Python from the [official website](https://www.python.org/downloads/). For Ubuntu, you can use the following command: `sudo apt-get update && sudo apt-get install python3 python3-pip`.

To install the application and its dependencies, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/athena-security/tnrg.git
   ```

2. Navigate into the cloned repository's backend directory:

   ```bash
   cd 03-API/ 
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv backend
   ```

4. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

   Before developing or deploying, make sure to update the `PORT` and `BAUD_RATE` in the `.env` file to match your system's configuration. The default settings are `PORT="/dev/tty.usbserial-120"` and `BAUD_RATE=1200`.

   Now, you're all set and ready to start developing or building!

### 💻 1) Development

To run the development server, use the following command:

```
python3 api.py
```

The application will be available at `http://localhost:5000/trng/randomNum/getRandom`.

### 🚀 2) Production

To deploy the application in a production environment, consider using a robust WSGI server like Gunicorn or uWSGI along with a reverse proxy like Nginx. Please refer to our [User Manual](../01-Documentation/USERGUIDE.md) for detailed instructions on deploying the application.



## License

This project is licensed under the [MIT License](https://chat.openai.com/LICENSE.md).