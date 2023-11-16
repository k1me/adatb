import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private baseUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  login(credentials: { felhasznalonev: string, jelszo: string }): Observable<any> {
    const url = `${this.baseUrl}/felhasznalo/login`;
    return this.http.post(url, credentials);
  }

  register(userData: { felhasznalonev: string, nev: string, jelszo: string }): Observable<any> {
    const url = `${this.baseUrl}/felhasznalo/register`;
    return this.http.post(url, userData);
  }
}