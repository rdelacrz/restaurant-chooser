import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Restaurant } from '../../models';
import { RestaurantService } from '../../core/services';

@Component({
  selector: 'restaurants',
  templateUrl: './restaurants.component.html',
  styleUrls: ['./restaurants.component.scss']
})
export class RestaurantsComponent implements OnInit {
  header = "Restaurants";
  restaurants : Restaurant[] = [];

  constructor(private restaurantService: RestaurantService, private router: Router) { }

  ngOnInit() {
    this.restaurantService.getRestaurants().subscribe(
      (res: any) => {
        this.restaurants = res;
      }
    );
  }

  onAddRestaurant() {
    this.router.navigateByUrl("add-restaurant");
  }
}
