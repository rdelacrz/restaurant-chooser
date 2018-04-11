import { Injectable } from '@angular/core';
import { ApiService } from './api.service';

@Injectable()
export class CuisineTypeService {
  private resourceBase = "cuisinetypes";

  constructor(private apiService: ApiService) { }

  getCuisineTypes() {
    return this.apiService.get(this.resourceBase);
  }
}