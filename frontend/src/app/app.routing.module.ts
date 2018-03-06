import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  //{ path: '', redirectTo: 'home', pathMatch: 'full' },
  //{ path: 'home', loadChildren: './components/home/home.module#HomeModule' },
  //{ path: 'restaurants', loadChildren: './components/restaurants/restaurants.module#RestaurantsModule' },
  //{ path: 'users', loadChildren: './components/users/users.module#UsersModule' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
