import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ReservationService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  getReservations() {
    return this.http.get<any[]>(this.apiUrl + '/foglalasok');
  }

  addReservation(reservation: any) {
    return this.http.post<any>(this.apiUrl + '/foglalas', reservation);
  }

  updateRoomStatus(email: string, mettol: any, meddig: any, selectedRooms: any[]) {
    const adatok = {
      email: email,
      mettol: mettol,
      meddig: meddig,
      selectedRooms: selectedRooms
    };
    console.log(adatok);
    return this.http.post<any>(this.apiUrl + '/szobaja', adatok);
  }

  handleReservation(reservation: any) {
    return this.http.post<any>(this.apiUrl + '/kezeli', reservation);
  }

  getOccupiedRooms() {
    return this.http.get<any[]>(this.apiUrl + '/szobaja');
  }

  deleteReservation(reservation: any) {
    return this.http.delete<any>(this.apiUrl + `/foglalas/${reservation.email}/${reservation.mettol}T00:00:00/${reservation.meddig}T00:00:00`);
  }
}