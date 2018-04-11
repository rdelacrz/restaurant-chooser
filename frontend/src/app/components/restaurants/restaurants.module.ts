import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';

import { SharedModule } from '../shared/shared.module';
import { RestaurantsRouting } from './restaurants.routing.module';

import { AddRestaurantComponent } from './add-restaurant/add-restaurant.component';
import { RestaurantsComponent } from './restaurants.component';


@NgModule({
  declarations: [
    AddRestaurantComponent,
    RestaurantsComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    RestaurantsRouting,
    SharedModule
  ]
})
export class RestaurantsModule { }
