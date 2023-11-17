import { Component } from '@angular/core';
import { RoomService } from '../services/room.service';

@Component({
  selector: 'app-room-type',
  templateUrl: './room-type.component.html',
  styleUrls: ['./room-type.component.scss']
})
export class RoomTypeComponent {
  rooms: any[] = [];
  roomTypes: any[] = [];

  constructor(private roomService: RoomService) {}

  ngOnInit(): void {
    this.roomService.getRooms().subscribe(rooms => {
      this.rooms = rooms;
    });

    this.roomService.getRoomTypes().subscribe(roomTypes => {
      this.roomTypes = roomTypes;
    });
  }
}
