import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';

import { AppRouting } from './app.routing.module';
import { CoreModule } from './core/core.module';
import { HomeModule } from './components/home/home.module';
import { RestaurantsModule } from './components/restaurants/restaurants.module';
import { SharedModule } from './components/shared/shared.module';
import { UsersModule } from './components/users/users.module';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    CommonModule,
    FormsModule,
    AppRouting,
    CoreModule,
    HomeModule,
    RestaurantsModule,
    SharedModule,
    UsersModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
