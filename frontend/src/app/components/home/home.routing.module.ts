import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent }
];

export const HomeRouting = RouterModule.forChild(routes);