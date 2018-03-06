import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { NavigationService } from './core/services';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = "RJH Restaurant Chooser";

  constructor(public navigationService: NavigationService, private router: Router) {}
}
