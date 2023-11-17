import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ReservationService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  getReservations() {
    return this.http.get<any[]>(this.apiUrl + '/foglalasok');
  }

  // További funkciók implementálása (szerkesztés, törlés stb.)
}