import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Rx';
import { UrlService } from './url.service'

@Injectable()
export class ApiService {
  constructor(private http: HttpClient, private urlService: UrlService) { }

  get(resourceUrl: string) {
    let url = this.urlService.apiUrl + resourceUrl;
    return this.http.get(url)
      .catch((error: Response) => Observable.throw(error || 'Server Error'));
  }

  post(resourceUrl: string, data: any) {
    let url = this.urlService.apiUrl + resourceUrl;
    return this.http.post(url, data)
      .catch((error: Response) => Observable.throw(error || 'Server Error'));
  }

  put(resourceUrl: string, data: any) {
    let url = this.urlService.apiUrl + resourceUrl;
    return this.http.put(url, data)
      .catch((error: Response) => Observable.throw(error || 'Server Error'));
  }

  delete(resourceUrl: string) {
    let url = this.urlService.apiUrl + resourceUrl;
    return this.http.delete(url)
      .catch((error: Response) => Observable.throw(error || 'Server Error'));
  }
}