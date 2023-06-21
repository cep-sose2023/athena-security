import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Title } from '@angular/platform-browser';

// Decorator that marks a class as an Angular component
@Component({
  selector: 'app-root', // The CSS selector that identifies this directive in a template
  templateUrl: './app.component.html', // The URL to the template file for this component
  styleUrls: ['./app.component.css'] // The list of URLs to stylesheets to be applied to this component's view
})
export class AppComponent {

  // Dependencies are injected via the constructor
  constructor(private router: Router, private titleService: Title) {}

  // Lifecycle hook that is called after data-bound properties of a directive are initialized
  ngOnInit() {
    // Set the title of the document (shown in browser tab)
    this.titleService.setTitle('trng');
  }

  // Getter to return the current URL path
  get currentRoute() {
    return this.router.url;
  }
}
