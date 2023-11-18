import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class GuestService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  getGuests() {
    return this.http.get<any[]>(this.apiUrl + '/vendegek');
  }

  addGuest(guest: any) {
    return this.http.post(this.apiUrl + '/vendeg', guest);
  }

  deleteGuest(email: number) {
    return this.http.delete(this.apiUrl + '/vendeg/' + email);
  }
}