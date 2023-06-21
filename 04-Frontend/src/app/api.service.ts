import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

// This service provides a layer of abstraction over the app's HTTP interactions
@Injectable({
  providedIn: 'root' // This service is provided at the root level, making it a singleton
})
export class ApiService {
  private baseApiUrl = 'https://172.16.78.59:8443/trng/randomNum'; // Base URL for the API

  constructor(private http: HttpClient) {} // Dependency Injection of HttpClient

  // Initialize the system by making a GET request to the API
  init(): Observable<any> {
    const url = `${this.baseApiUrl}/init`;
    return this.http.get(url).pipe(
      catchError(error => this.handleError(error)) // Handle any errors from the request
    );
  }

  // Shutdown the system by making a GET request to the API
  shutdown(): Observable<any> {
    const url = `${this.baseApiUrl}/shutdown`;
    return this.http.get(url).pipe(
      catchError(error => this.handleError(error)) // Handle any errors from the request
    );
  }

  // Restart the system by making a GET request to the API
  restart(): Observable<any> {
    const url = `${this.baseApiUrl}/restart`;
    return this.http.get(url).pipe(
      catchError(error => this.handleError(error)) // Handle any errors from the request
    );
  }

  // Get a set of random numbers from the API
  getRandomNumbers(numBits?: string, quantity?: string): Observable<string[]> {
    const url = `${this.baseApiUrl}/getRandom?numBits=${numBits}&quantity=${quantity}`;
    return this.http.get<string[]>(url).pipe(
      catchError(error => this.handleError(error)) // Handle any errors from the request
    );
  }

  // Generate test data by making a GET request to the API
  generateTestdata(numBits?: string, filetype: string = 'bin'): Observable<any> {
    const url = `${this.baseApiUrl}/generateTestdata?numBits=${numBits}&filetype=${filetype}`;
    return this.http.get(url).pipe(
      catchError(error => this.handleError(error)) // Handle any errors from the request
    );
  }

  // Handle any errors that may come from the API
  private handleError(error: any): Observable<never> {
    let errorMessage = 'Unknown error occurred';
    // Error messages based on status code
    if (error.status === 432) {
      errorMessage = 'Service is currently unavailable';
    } else if (error.status === 500) {
      errorMessage = 'Internal server error occurred';
    } else if (error.status === 555) {
      errorMessage = 'Error while generating data';
    }
    // Error messages based on error message or error error properties
    if (error.error) {
      if (error.error.message) {
        errorMessage = error.error.message;
      } else if (error.error.error) {
        errorMessage = error.error.error;
      }
    }
    return throwError(errorMessage); // Propagate the error to the caller
  }
}
