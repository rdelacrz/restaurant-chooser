import { Injectable } from '@angular/core';
import { ApiService } from './api.service';
import { FullUserData } from '../../view-models';

@Injectable()
export class UserService {
  private resourceBase = "users";

  constructor(private apiService: ApiService) { }

  getUsers() {
    return this.apiService.get(this.resourceBase);
  }

  getUserById(id: number) {
    return this.apiService.get(this.resourceBase + "/" + id);
  }

  createUser(parameters: FullUserData) {
    return this.apiService.post(this.resourceBase, parameters);
  }
}