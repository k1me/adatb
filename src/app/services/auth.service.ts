import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private baseUrl = 'http://localhost:8000';
  private loggedInUser: boolean = false;

  constructor(private http: HttpClient) { }

  login(credentials: { felhasznalonev: string, jelszo: string }): Observable<any> {
    const url = `${this.baseUrl}/felhasznalo/login`;
    this.loggedInUser = true;
    return this.http.post(url, credentials);
  }

  logout() {
    sessionStorage.removeItem('loginToken');
    this.loggedInUser = false;
  }

  register(userData: { felhasznalonev: string, nev: string, jelszo: string }): Observable<any> {
    const url = `${this.baseUrl}/felhasznalo/register`;
    return this.http.post(url, userData);
  }

  isLoggedIn() {
    return sessionStorage.getItem('loginToken') !== null;
  }

  getUser(felhasznalonev: string): Observable<any> {
    const url = `${this.baseUrl}/felhasznalo/${felhasznalonev}`;
    return this.http.get(url);
  }
}