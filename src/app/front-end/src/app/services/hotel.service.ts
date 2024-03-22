// hotel.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HotelService {
  private apiUrl = 'http://localhost:8000/api/hotels/';

  constructor(private http: HttpClient) {}

  getHoteles(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}
