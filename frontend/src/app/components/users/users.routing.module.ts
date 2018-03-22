import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { UsersComponent } from './users.component';
import { AddUserComponent } from './add-user/add-user.component';

const routes: Routes = [
  { path: 'users', component: UsersComponent },
  { path: 'add-user', component: AddUserComponent }
];

export const UsersRouting = RouterModule.forChild(routes);
