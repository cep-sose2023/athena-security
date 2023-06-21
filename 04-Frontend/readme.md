# TRNG: Frontend (Angular Single-Page Application)

---

This is an Angular Single-Page Application (SPA) that provides functionality for system control, generating random numbers, and downloading files. The application communicates with the Athena-Security True Random Number Generator (TRNG) backend API server to perform these operations.



## 🖨️ Technologies Used

This part of the TRNG is a Single Page Application (SPA) built using:

- Angular: A TypeScript-based web application framework used for building the SPA.
- TypeScript: A statically typed superset of JavaScript used for writing the application code.
- HTML5: Markup language used for defining the structure and layout of the application's user interface.
- CSS3: Stylesheet language used for styling and formatting the HTML elements.
- RxJS: A library for reactive programming using Observables, used for handling asynchronous operations.
- HttpClient: An Angular module for making HTTP requests to the backend API server.



## ⭐ Features

The True Random Number Generator (TRNG) frontend offers a clean, interactive user interface for generating and downloading random numbers. It consists of the following components:

1. 🖥️ System Control
   - Initialize the system
   - Shutdown the system
   - Restart the system
2. 🔢 Generate Random Numbers
   - Generate random numbers based on the provided parameters (number of bits and quantity)
3. 💾 Download Files
   - Generate downloadable files of random numbers by specifying the number of bits and file type (binary or text)
   - Download the generated file from the backend API server



## 🛠️ Installation

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 15.2.8. To get started with the application, make sure you have the following requirements installed:

1. **Node.js**: Node.js is used to run the development server and build the frontend project. Install Node.js from the [official website](https://nodejs.org/). . For Ubuntu, you can use the following command: `sudo apt-get update && sudo apt-get install nodejs npm`.

1. **Angular CLI**: Angular CLI is a command-line interface for Angular and is used to serve the application during development, and to build the application for production. After Node.js is installed, install Angular CLI globally using npm (Node Package Manager): `npm install -g @angular/cli`.

Please note that the backend service is required for the frontend to function properly. Make sure to set up and start the backend service before using the frontend application.

To install the application and its dependencies, follow these steps:


1. Clone the repository:

   ```bash
   git clone https://github.com/athena-security/tnrg.git
   ```

2. Navigate into the cloned repository.

   ```bash
   cd 04-Frontend/ 
   ```

3. Install dependencies:

   ```bash
   npm install
   ```

   Now, you're all set and ready to start developing or building!

### 💻 1) Development

To run a development server, use the following command:

```
ng serve
```

The application will be available at `http://localhost:4200/`. The server automatically reloads the application when any of the source files are changed

### 🚀 2) Build

Before building, make sure to update the base API URL in the `ApiService` file (`api.service.ts`) and the form action in the `DownloadNumbersComponent` file (`downloadnumbers.component.html`) to match your backend server URL.

Once the URLs are correctly set, you can build a production-ready version of the frontend using the Angular CLI's build command.

```
ng build --prod
```

This will create a `dist/` directory with all the compiled and minified assets ready to be served by a web server. For a detailed step-by-step deployment guide, please refer to our [User Manual](../01-Documentation/USERGUIDE.md). It provides extensive instructions and guidance on deploying the application, configuring the environment, and more.



## License

This project is licensed under the [MIT License](../LICENSE.md).





