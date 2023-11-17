import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class RoomService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  getRooms() {
    return this.http.get<any[]>(this.apiUrl + '/szobak');
  }
  
  getRoomTypes() {
    return this.http.get<any[]>(this.apiUrl + '/szobatipusok');
  }
}
