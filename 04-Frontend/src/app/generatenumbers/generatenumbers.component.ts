import { Component } from '@angular/core';
import {ApiService} from "../api.service";

@Component({
  selector: 'app-generatenumbers',
  templateUrl: './generatenumbers.component.html',
  styleUrls: ['./generatenumbers.component.css']
})

// The GeneratenumbersComponent handles the random number generation functionality
export class GeneratenumbersComponent {
  showStatusContainer: boolean = false; // State to control visibility of the status container
  status: string = ''; // String to hold status message
  error: string = ''; // String to hold error message
  generatedNumbers: string[] = []; // Array to hold the generated random numbers

  constructor(private api: ApiService) { } // Dependency Injection of ApiService

  // Method to trigger random number generation with given bits and quantity
  generateRandomNumbers(numBits: string, quantity: string): void {
    this.error = ""
    this.status = 'Random number generation in progess...'
    this.showStatusContainer = true;
    // Call to ApiService's getRandomNumbers method
    this.api.getRandomNumbers(numBits, quantity).subscribe(
      (response) => {
        // Update generatedNumbers with response
        this.generatedNumbers = response;
        this.status = 'Random numbers generated successfully';
        this.showStatusContainer = true;
      },
      (error) => {
        // Update error message with actual error message from the server
        this.error = error;
        this.status = 'An error occurred while generating random numbers: ';
        this.showStatusContainer = true;
      }
    );
  }
}
