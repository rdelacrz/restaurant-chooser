import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { SharedModule } from '../shared/shared.module';
import { UsersRouting } from './users.routing.module';

import { UsersComponent } from './users.component';
import { AddUserComponent } from './add-user/add-user.component';

@NgModule({
  declarations: [
    UsersComponent,
    AddUserComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    SharedModule,
    UsersRouting
  ]
})
export class UsersModule { }
