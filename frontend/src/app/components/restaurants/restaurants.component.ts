import { Component, OnInit } from '@angular/core';
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

  constructor(private restaurantService: RestaurantService) { }

  ngOnInit() {
    this.restaurantService.getRestaurants().subscribe(
      (res: any) => {
        this.restaurants = res;
      }
    );
  }

}
