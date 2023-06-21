# TRNG: NodeMCU Sensor Data Sender

This is an Arduino sketch written in C++ for a NodeMCU development board, a low-cost open-source IoT platform. It leverages built-in functionalities of the NodeMCU to control an LED and a fan, read analog sensor data, and send this data over a serial interface. The program reads the solar voltage from a sensor, extracts the least significant bits (LSBs), and sends them over the serial interface.



## 🖨️ Technologies Used

This project is built using:

- **Arduino IDE:** A software platform used for writing and uploading code to development boards, which are part of electronics projects. The Arduino IDE provides a comprehensive toolset for microcontroller programming, simplifying the process of coding and debugging.
- **C++:** The main programming language used in the Arduino IDE.
- **NodeMCU:** An open-source IoT platform. It includes firmware which runs on the ESP8266 Wi-Fi SoC from Espressif Systems, and hardware which is based on the ESP-12 module.

## ⭐ Features

The NodeMCU code includes the following features:

- 🖥️ **LED & Fan Control:** Ability to turn ON and OFF the LED and the fan by receiving commands over the serial interface.
- 📊 **Analog Sensor Reading:** The program reads the solar voltage from an analog sensor, processes the reading, and converts it to an integer.
- 📡 **Data Transmission:** The program transmits the processed sensor data over the serial interface.



## 🛠️ Installation

This project was written in the Arduino IDE. To run the code on your NodeMCU, make sure you have the following requirements:

- **Arduino IDE:** Arduino IDE is a software used to write and upload the program to the NodeMCU board. Download and install Arduino IDE from the [official website](https://www.arduino.cc/en/software).
- **NodeMCU ESP8266:** The sketch is intended to be run on a NodeMCU board. You can purchase the board from any reputed electronics supplier.

 After you have the necessary tools, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/athena-security/cep.git
   ```

2. **Open the sketch in the Arduino IDE:** Navigate to the downloaded location and open the "nodemcu.ino" file.

3. **Set up the board:** Go to File > Preferences, in the "Additional Boards Manager URLs" field, add this link: "http://arduino.esp8266.com/stable/package_esp8266com_index.json" and click OK. Now, go to Tools > Board > Boards Manager, search for ESP8266 and install it. 

4. **Select the board:** Go to Tools > Board > ESP8266 Boards > NodeMCU 1.0 (ESP-12E Module).

5. **Select the port:** Go to Tools > Port > Select the COM Port that the NodeMCU is connected to.

6. **Upload the sketch:** Click on the upload button (->) or select Sketch > Upload from the menu.

Once the upload is complete, the LED and the fan should respond to "on" and "off" commands sent over the serial interface, and transmit processed sensor data when active.

⚠️ Note: Ensure you have the necessary components and have configured the NodeMCU board correctly before uploading the code. A complete construction manual with a schematic also exists in this repository.



## License

This project is licensed under the [MIT License](../LICENSE.md).
