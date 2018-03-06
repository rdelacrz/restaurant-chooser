import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { SharedModule } from '../shared/shared.module';
import { RestaurantsRoutingModule } from './restaurants.routing.module';

import { RestaurantsComponent } from './restaurants.component';


@NgModule({
  declarations: [
    RestaurantsComponent
  ],
  imports: [
    CommonModule,
    RestaurantsRoutingModule,
    SharedModule
  ]
})
export class RestaurantsModule { }
