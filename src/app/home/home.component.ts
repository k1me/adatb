import { Component, OnInit } from '@angular/core';
import { GuestService } from '../services/guest.service';
import { ReservationService } from '../services/reservation.service';
import { AuthService } from '../services/auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  guests: any[] = [];
  reservations: any[] = [];
  user: any = null;

  constructor(private guestService: GuestService, private reservationService: ReservationService, private authService: AuthService) { }

  getToken(): null | string {
    return sessionStorage.getItem('loginToken');
  }

  ngOnInit(): void {
    this.guestService.getGuests().subscribe(users => {
      this.guests = users;
    });

    this.reservationService.getReservations().subscribe(reservations => {
      this.reservations = reservations;
    });

    const token = this.getToken();

    if (token) {
      this.authService.getUser(token).subscribe(user => {
        this.user = user;
      });
    }
  }

}