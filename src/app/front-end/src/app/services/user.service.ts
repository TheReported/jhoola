import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class UserService {
    constructor(private http: HttpClient) { }

    getUserData(clientId: number): Observable<any> {
        let apiUrl = `http://localhost:8000/api/clients/${clientId}`;
        return this.http.get<any>(apiUrl);
    }
}
