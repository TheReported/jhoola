import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private baseUrl = 'http://localhost:8000/login/';

  constructor(private http: HttpClient) { }

  login(hotelSlug: string, data: any) {
    const loginUrl = `${this.baseUrl}${hotelSlug}/`;
    return this.http.post(loginUrl, data);
  }
}
