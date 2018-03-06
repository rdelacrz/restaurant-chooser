import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { ApiService, CommonService, ListItemService, NavigationService, RestaurantService, UrlService, UserService } 
  from './services';

@NgModule({
  imports: [
    HttpClientModule
  ],
  providers: [
    ApiService,
    CommonService,
    ListItemService,
    NavigationService,
    RestaurantService,
    UrlService,
    UserService
  ]
})
export class CoreModule {}