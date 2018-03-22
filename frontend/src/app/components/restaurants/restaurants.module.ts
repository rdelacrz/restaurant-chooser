import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { SharedModule } from '../shared/shared.module';
import { RestaurantsRouting } from './restaurants.routing.module';

import { RestaurantsComponent } from './restaurants.component';


@NgModule({
  declarations: [
    RestaurantsComponent
  ],
  imports: [
    CommonModule,
    RestaurantsRouting,
    SharedModule
  ]
})
export class RestaurantsModule { }
