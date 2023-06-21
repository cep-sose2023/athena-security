import { Component } from '@angular/core';
import {ApiService} from "../api.service";

@Component({
  selector: 'app-downloadnumbers',
  templateUrl: './downloadnumbers.component.html',
  styleUrls: ['./downloadnumbers.component.css']
})
// DownloadnumbersComponent is responsible for generating a downloadable file of random numbers
export class DownloadnumbersComponent {

  showStatusContainer: boolean = false; // State to control the visibility of the status container
  showDownloadButton: boolean = false; // State to control the visibility of the download button
  status: string = ''; // String to hold status message
  error: string = ''; // String to hold error message

  constructor(private api: ApiService) { } // Dependency Injection of ApiService

  // Method to generate a downloadable file with a specified number of bits and filetype
  generateDownloadableFile(numBits: string, filetype: string): void {
    this.showDownloadButton = false;
    this.showStatusContainer = true;
    this.error = ""
    this.status = 'Downloadable file is being generated...'
    // Call to ApiService's generateTestdata method
    this.api.generateTestdata(numBits, filetype).subscribe(
      (response: any) => {
        this.status = response.message;
        this.showDownloadButton = true;
        this.showStatusContainer = true;
      },
      (error) => {
        // Update error message with actual error message from the server
        this.error = error;
        this.status = 'An error occurred while generating the downloadable file: ';
        this.showStatusContainer = true;
      });
  }
}
