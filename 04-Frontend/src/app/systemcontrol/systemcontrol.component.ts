import {Component} from '@angular/core';
import {ApiService} from "../api.service";

@Component({
  selector: 'app-systemcontrol',
  templateUrl: './systemcontrol.component.html',
  styleUrls: ['./systemcontrol.component.css']
})

// The SystemControlComponent handles the control of the system's state. This includes starting,
// stopping, restarting and retrieving the status of the system
export class SystemcontrolComponent {
  showStatusContainer: boolean = false; // State to control visibility of the status container
  status: string = ''; // String to hold status message
  error: string = ''; // String to hold error message

  // Dependency Injection of ApiService
  constructor(private api: ApiService) { }

  // Function to initialize the system
  initSystem(): void {
    this.error = '';
    this.status = 'Initialising system...';
    this.showStatusContainer = true;
    this.api.init().subscribe(
      (response: any) => {
        // Update status with server response or default success message
        this.status = response.message || 'System initialised successfully';
      },
      (error) => {
        // Update error message with actual error message from the server
        this.error = error;
        this.status = 'An error occurred while initialising the system: ';
      });
  }

  // Function to shut down the system
  shutdownSystem(): void {
    this.error = '';
    this.status = 'Shutting down system...';
    this.showStatusContainer = true;
    this.api.shutdown().subscribe(
      (response: any) => {
        // Update status with server response or default success message
        this.status = response.message || 'System successfully shutdown';
        this.error = '';
      },
      (error) => {
        // Update error message with actual error message from the server
        this.error = error;
        this.status = 'An error occurred while shutting down the system:';
      });
  }

  // Function to restart the system
  restartSystem(): void {
    this.error = '';
    this.status = 'Restarting system...';
    this.showStatusContainer = true;
    this.api.restart().subscribe(
      (response: any) => {
        // Update status with server response or default success message
        this.status = response.message || 'System successfully restarted';
        this.error = '';
      },
      (error) => {
        // Update error message with actual error message from the server
        this.error = error;
        this.status = 'An error occurred while restarting the system: ';
      });
  }
}
