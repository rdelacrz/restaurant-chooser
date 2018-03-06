import { Injectable } from '@angular/core';
import { ApiService } from './api.service';

@Injectable()
export class ListItemService {
  private resourceBase = "listitems";

  constructor(private apiService: ApiService) { }

  getListItems() {
    return this.apiService.get(this.resourceBase);
  }

  getListItemById(id: number) {
    return this.apiService.get(this.resourceBase + "/" + id);
  }

  getStates() {
    return this.apiService.get(this.resourceBase + "/states");
  }

  getWeekdays() {
    return this.apiService.get(this.resourceBase + "/weekdays");
  }
}