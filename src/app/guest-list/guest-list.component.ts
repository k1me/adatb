import { Component } from '@angular/core';
import { GuestService } from '../services/guest.service';

@Component({
  selector: 'app-guest-list',
  templateUrl: './guest-list.component.html',
  styleUrls: ['./guest-list.component.scss']
})
export class GuestListComponent {
  guests: any[] = [];
  newGuest = {
    email: '',
    nev: '',
    telefonszam: '',
    szuletesi_datum: new Date()
  };

  constructor(private guestService: GuestService) {}

  ngOnInit(): void {
    this.guestService.getGuests().subscribe(users => {
      this.guests = users;
    });
  }

  loadGuests(): void {
    this.guestService.getGuests().subscribe(guests => this.guests = guests);
  }

  addNewGuest(): void {
    this.guestService.addGuest(this.newGuest).subscribe(() => {
      this.newGuest = {
        email: '',
        nev: '',
        telefonszam: '',
        szuletesi_datum: new Date()
      };
    });
  }

  deleteGuest(email: string): void {
    this.guestService.deleteGuest(email).subscribe(() => {
      this.loadGuests();
    });
  }

}