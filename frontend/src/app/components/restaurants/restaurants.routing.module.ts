import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AddRestaurantComponent } from './add-restaurant/add-restaurant.component';
import { RestaurantsComponent } from './restaurants.component';

const routes: Routes = [
  { path: 'restaurants', component: RestaurantsComponent },
  { path: 'add-restaurant', component: AddRestaurantComponent }
];

export const RestaurantsRouting = RouterModule.forChild(routes);
