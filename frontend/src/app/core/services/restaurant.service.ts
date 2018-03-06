import { Injectable } from '@angular/core';
import { ApiService } from './api.service';

@Injectable()
export class RestaurantService {
  private resourceBase = "restaurants";

  constructor(private apiService: ApiService) { }

  getRestaurants() {
    return this.apiService.get(this.resourceBase);
  }

  getRestaurantById(id: number) {
    return this.apiService.get(this.resourceBase + "/" + id);
  }

  createRestaurants(parameters: any) {
    return this.apiService.post(this.resourceBase, parameters);
  }
}