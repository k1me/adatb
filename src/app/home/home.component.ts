import { Component, OnInit } from '@angular/core';
import { GuestService } from '../services/guest.service';
import { ReservationService } from '../services/reservation.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  guests: any[] = [];
  reservations: any[] = [];

  constructor(private guestService: GuestService, private reservationService: ReservationService) {}

  ngOnInit(): void {
    this.guestService.getUsers().subscribe(users => {
      this.guests = users;
    });

    this.reservationService.getReservations().subscribe(reservations => {
      this.reservations = reservations;
    });
  }

  // Itt implementáld a további funkciókat (pl. szerkesztés, törlés stb.)
}