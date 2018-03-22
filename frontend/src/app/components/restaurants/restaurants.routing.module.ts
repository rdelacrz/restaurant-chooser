import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RestaurantsComponent } from './restaurants.component';

const routes: Routes = [
  { path: 'restaurants', component: RestaurantsComponent }
];

export const RestaurantsRouting = RouterModule.forChild(routes);
