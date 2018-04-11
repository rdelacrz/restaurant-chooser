import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ApiService, CommonService, CuisineTypeService, ListItemService, ModalService, NavigationService, RestaurantService, 
  UrlService, UserService } from './services';

@NgModule({
  imports: [
    HttpClientModule,
    NgbModule.forRoot()
  ],
  providers: [
    ApiService,
    CommonService,
    CuisineTypeService,
    ListItemService,
    ModalService,
    NavigationService,
    RestaurantService,
    UrlService,
    UserService
  ]
})
export class CoreModule {}