import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Room } from '../interfaces/room.interface';

@Injectable({
  providedIn: 'root'
})
export class RoomService {

  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  getRooms() {
    return this.http.get<any[]>(this.apiUrl + '/szobak');
  }

  getRoomTypes() {
    return this.http.get<any[]>(this.apiUrl + '/szobatipusok');
  }

  getRoomPrice(roomType: string) {
    return this.http.get<any>(this.apiUrl + '/szobatipus/' + roomType);
  }

}
