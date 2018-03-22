import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  animationTriggered = false;

  constructor() { }

  ngOnInit() {
    setTimeout(()=> this.triggerAnimation(), 100);
  }

  triggerAnimation() {
    this.animationTriggered = true;
  }
}
