import { Injectable } from '@angular/core';

@Injectable()
export class NavigationService {
  constructor() {}

  public isCollapsed = false;

  toggleNavBar() {
    this.isCollapsed = !this.isCollapsed;
  }
}