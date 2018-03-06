import { Injectable } from '@angular/core';

import { environment } from '../../../environments/environment';

@Injectable()
export class UrlService {
  constructor() { }

  apiUrl = environment.baseUrl + "api/"
}