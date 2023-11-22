import { Component } from '@angular/core';
import { RoomService } from '../services/room.service';
import { ReservationService } from '../services/reservation.service';
import { GuestService } from '../services/guest.service';

@Component({
  selector: 'app-queries',
  templateUrl: './queries.component.html',
  styleUrls: ['./queries.component.scss']
})
export class QueriesComponent {
  rooms : any = {};
  filteredReservations: any = {};
  eldestGuest: any = {};
  eldestGuestList: any[] = [];

  constructor( private roomService: RoomService, private reservationService: ReservationService, private guestService: GuestService) { }

  ngOnInit(): void {
    this.roomService.getRoomSummary().subscribe((data: any) => {
      this.rooms = data;
    });
    this.reservationService.getFilteredReservations().subscribe((data: any) => {
      this.filteredReservations = data;
    });
    this.guestService.getEldestGuest().subscribe((data: any) => {
      this.eldestGuest = data;
      this.eldestGuestList = [this.eldestGuest]
    });
  }

  objectKeys(obj: object): string[] {
    return Object.keys(obj);
  }
}
