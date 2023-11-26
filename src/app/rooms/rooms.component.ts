import { Component } from '@angular/core';
import { RoomService } from '../services/room.service';
import { ReservationService } from '../services/reservation.service';

@Component({
  selector: 'app-rooms',
  templateUrl: './rooms.component.html',
  styleUrls: ['./rooms.component.scss']
})
export class RoomsComponent {
  rooms: any[] = [];
  occupiedRooms: Map<number, boolean> = new Map<number, boolean>();
  todaysDate = new Date();

  constructor(private roomService: RoomService, private reservationService: ReservationService) { }

  ngOnInit(): void {
    this.roomService.getRooms().subscribe(rooms => {
      this.rooms = rooms.sort((a, b) => a.szobaszam - b.szobaszam);
      this.loadOccupiedRooms();
    });
  }

  private loadOccupiedRooms() {

    this.reservationService.getOccupiedRooms().subscribe(occupiedRooms => {
      occupiedRooms.forEach(room => {
        const dateFrom = new Date(room.mettol);
        const dateTo = new Date(room.meddig);
        if (dateFrom < this.todaysDate && dateTo > this.todaysDate) {
          this.occupiedRooms.set(room.szobaszam, true);
        }
      });
    })
  }

  isRoomOccupied(szobaszam: number): boolean {
    return this.occupiedRooms.get(szobaszam) || false;
  }
}