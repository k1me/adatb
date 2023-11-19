import { Component } from '@angular/core';
import { RoomService } from '../services/room.service';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-room-type',
  templateUrl: './room-type.component.html',
  styleUrls: ['./room-type.component.scss']
})
export class RoomTypeComponent {
  rooms: any[] = [];
  roomTypes: any[] = [];
  listRoomTypes: any[] = [];
  selectedRoomType: any;
  roomForm: FormGroup;
  napi_ar: number = 0;


  reloadPage(): void {
    window.location.reload();
  }

  constructor(private roomService: RoomService, private formBuilder: FormBuilder) {
    this.roomForm = this.formBuilder.group({
      napi_ar: 0
    });
  }

  ngOnInit(): void {
    this.roomService.getRooms().subscribe(rooms => {
      this.rooms = rooms;
    });

    this.roomService.getRoomTypes().subscribe(roomTypes => {
      this.roomTypes = roomTypes;
    });
  }

  updateDailyPrice(roomType: any, napi_ar: number): void {
    roomType.napi_ar = napi_ar;

    this.roomService.updateRoomType(roomType, napi_ar).subscribe(() => {
      this.reloadPage()
    });
  }
}
