import { Component } from '@angular/core';
import { GuestService } from '../services/guest.service';

@Component({
  selector: 'app-guest-list',
  templateUrl: './guest-list.component.html',
  styleUrls: ['./guest-list.component.scss']
})
export class GuestListComponent {
  guests: any[] = [];

  constructor(private guestService: GuestService) {}

  ngOnInit(): void {
    this.guestService.getUsers().subscribe(users => {
      this.guests = users;
    });
  }
}
