import { Component } from '@angular/core';
import { ReservationService } from '../services/reservation.service';
import { GuestService } from '../services/guest.service';
import { RoomService } from '../services/room.service';
@Component({
  selector: 'app-reservation',
  templateUrl: './reservation.component.html',
  styleUrls: ['./reservation.component.scss']
})
export class ReservationComponent {
  reservations: any[] = [];

  guests: any[] = [];

  roomTypes: any[] = [];

  selectedRoomType: string = '';

  rooms: any[] = [];

  restOfTheRooms: any[] = [];
  
  
  constructor(private reservationService: ReservationService, private guestService: GuestService, private roomService: RoomService) {}

  ngOnInit(): void {
    this.reservationService.getReservations().subscribe(reservations => {
      this.reservations = reservations;
    });

    this.getGuests()
    this.getRoomTypes()
    this.getRooms()
    this.updateRestOfTheRooms()
  }

  addNewReservation(): void {}

  getRooms(): void {
    this.roomService.getRooms().subscribe(rooms => {
      this.rooms = rooms;
    });
  }

  getGuests(): void {
    this.guestService.getGuests().subscribe(guests => {
      this.guests = guests;
    });
  }

  getRoomTypes():void {
    this.roomService.getRoomTypes().subscribe(roomTypes => {
      this.roomTypes = roomTypes;
    });
  }

  updateSelectedRoomType(roomType: any): void {
    this.selectedRoomType = roomType;
    this.updateRestOfTheRooms();
  }
  updateRestOfTheRooms(): void {
  this.restOfTheRooms = this.rooms.filter(room => room.megnevezes === this.selectedRoomType);
}
}
