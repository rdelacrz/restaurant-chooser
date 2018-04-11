import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Restaurant } from '../../../models';
import { CuisineTypeService, ListItemService, RestaurantService, UserService } from '../../../core/services';

@Component({
  selector: 'add-restaurant',
  templateUrl: './add-restaurant.component.html',
  styleUrls: ['./add-restaurant.component.scss']
})
export class AddRestaurantComponent implements OnInit {
  header = "Add Restaurant";
  model = new Restaurant(null, null, null, null, null, null, null, null, null);

  // Dropdowns
  cuisineTypes : any;
  states : any;
  users : any;

  constructor(private cuisineTypeService: CuisineTypeService, private listItemService: ListItemService, 
    private restaurantService: RestaurantService, private userService: UserService, private router: Router) { }

  ngOnInit() {
    this.cuisineTypes = this.cuisineTypeService.getCuisineTypes();
    this.states = this.listItemService.getStates();
    this.users = this.userService.getUsers();
  }

  onSubmit() {
    
  }

  onCancel() {
    this.goToRestaurantsScreen();
  }

  onClear() {
    this.model.clear();
  }

  private goToRestaurantsScreen() {
    this.router.navigateByUrl("restaurants")
  }
}