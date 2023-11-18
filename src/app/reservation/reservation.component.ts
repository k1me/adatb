import { Component } from '@angular/core';
import { ReservationService } from '../services/reservation.service';
import { GuestService } from '../services/guest.service';
import { RoomService } from '../services/room.service';
import { Room } from '../interfaces/room.interface';
import { Observable, map } from 'rxjs';
@Component({
  selector: 'app-reservation',
  templateUrl: './reservation.component.html',
  styleUrls: ['./reservation.component.scss']
})
export class ReservationComponent {
  reservations: any[] = [];
  guests: any[] = [];
  rooms: any[] = [];
  roomTypes: any[] = [];
  selectedEmail: string = '';
  selectedRoomType: string = '';
  selectedRoomNumber: number = 0;
  restOfTheRooms: any[] = [];
  selectedRooms: Room[] = [];
  sumNapiAr: number = 0;
  mettol = new Date();
  meddig = new Date();

  constructor(private reservationService: ReservationService, private guestService: GuestService, private roomService: RoomService) { }

  ngOnInit(): void {
    this.reservationService.getReservations().subscribe(reservations => {
      this.reservations = reservations;
    });

    this.getGuests()
    this.getRoomTypes()
    this.getRooms()
    this.updateRestOfTheRooms()
  }

  reloadPage(): void {
    window.location.reload();
  }

  addNewReservation(): void {
    this.sumNapiAr = 0;

    const getPricePromises = this.selectedRooms.map(room => {
      return new Promise<number>((resolve) => {
        this.getRoomPrice(room.megnevezes).subscribe(napi_ar => {
          this.sumNapiAr += napi_ar;
          resolve(napi_ar);
        });
      });
    });

    const mettolDate = new Date(this.mettol);
    const meddigDate = new Date(this.meddig);

    const isoStringMettol = mettolDate.toISOString().split('T')[0];
    const isoStringMeddig = meddigDate.toISOString().split('T')[0];

    Promise.all(getPricePromises).then(() => {

      const reservation = {
        email: this.selectedEmail,
        mettol: isoStringMettol,
        meddig: isoStringMeddig,
        fizetendo: this.sumNapiAr * (meddigDate.getTime() - mettolDate.getTime()) / (1000 * 60 * 60 * 24)
      };

      this.reservationService.addReservation(reservation).subscribe(() => {
        const roomInfo = {
          email: this.selectedEmail,
          mettol: isoStringMettol,
          meddig: isoStringMeddig,
          szobaszam: this.selectedRoomNumber
        }

        this.reservationService.updateRoomStatus(roomInfo).subscribe(() => {
          const handleReservation = {
            felhasznalonev: sessionStorage.getItem('loginToken'),
            email: this.selectedEmail,
            mettol: isoStringMettol,
            meddig: isoStringMeddig
          }

          this.reservationService.handleReservation(handleReservation).subscribe(() => {
            this.reloadPage();
          })
        })
      })
    })
  }

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

  getRoomTypes(): void {
    this.roomService.getRoomTypes().subscribe(roomTypes => {
      this.roomTypes = roomTypes;
    });
  }

  updateSelectedRoomType(roomType: any): void {
    this.selectedRoomType = roomType;
    this.updateRestOfTheRooms();
    this.updateSelectedRoomNumber(this.restOfTheRooms[0].szobaszam);
  }

  updateRestOfTheRooms(): void {
    this.restOfTheRooms = this.rooms.filter(room => room.megnevezes === this.selectedRoomType);
  }

  updateSelectedRoomNumber(roomNumber: any): void {
    this.selectedRoomNumber = roomNumber;
  }

  addRoomToList(): void {
    this.getRoomPrice(this.selectedRoomType).subscribe(napi_ar => {
      const szoba: Room = {
        megnevezes: this.selectedRoomType,
        szobaszam: this.selectedRoomNumber,
      };
      this.selectedRooms.push(szoba);
    });
  }

  deleteRoomFromList(room: Room): void {
    this.selectedRooms = this.selectedRooms.filter(szoba => szoba.szobaszam !== room.szobaszam);
    this.restOfTheRooms.push(room);
  }

  getRoomPrice(roomType: string): Observable<number> {
    return this.roomService.getRoomPrice(roomType).pipe(
      map(room => room.napi_ar)
    );
  }
}