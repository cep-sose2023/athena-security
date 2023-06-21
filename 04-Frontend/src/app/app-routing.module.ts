import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router'; // Angular modules for routing
import {GeneratenumbersComponent} from "./generatenumbers/generatenumbers.component"; // Component to handle random number generation
import {SystemcontrolComponent} from "./systemcontrol/systemcontrol.component"; // Component to handle system control
import {DownloadnumbersComponent} from "./downloadnumbers/downloadnumbers.component"; // Component to handle download of random numbers

// Define the routes for the application
const routes: Routes = [
  { path: '', redirectTo: 'generate', pathMatch: 'full' }, // Default path redirects to 'generate'
  { path: 'generate', component: GeneratenumbersComponent }, // 'generate' path leads to GeneratenumbersComponent
  { path: 'download', component: DownloadnumbersComponent }, // 'download' path leads to DownloadnumbersComponent
  { path: 'system', component: SystemcontrolComponent } // 'system' path leads to SystemcontrolComponent
  //{path: '**', component: PageNotFoundComponent} // Uncomment this for a catch-all route
];

@NgModule({
  imports: [RouterModule.forRoot(routes)], // Import routes
  exports: [RouterModule] // Export RouterModule to make it available throughout the application
})
export class AppRoutingModule { }
