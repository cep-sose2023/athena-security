import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module'; // Handles routing for the application
import { AppComponent } from './app.component'; // Main application component
import { SystemcontrolComponent } from './systemcontrol/systemcontrol.component'; // Component to handle system control
import { GeneratenumbersComponent } from './generatenumbers/generatenumbers.component'; // Component to handle random number generation
import { DownloadnumbersComponent } from './downloadnumbers/downloadnumbers.component'; // Component to handle download of random numbers
import {ApiService} from "./api.service"; // Service to handle API calls
import {HttpClientModule} from "@angular/common/http"; // Angular module for making HTTP requests

@NgModule({
  declarations: [
    AppComponent,
    SystemcontrolComponent,
    GeneratenumbersComponent,
    DownloadnumbersComponent
    // Declares the components to be used in this module
  ],
  imports: [
    BrowserModule, // Basic Angular module for working with the browser
    AppRoutingModule, // Routing module
    HttpClientModule // HTTP client module for making API calls
  ],
  providers: [ApiService], // Register ApiService as a provider
  bootstrap: [AppComponent] // AppComponent is the root component of this Angular module
})
export class AppModule { }
