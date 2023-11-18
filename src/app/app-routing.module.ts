import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { HomeComponent } from './home/home.component';
import { GuestListComponent } from './guest-list/guest-list.component';
import { ReservationComponent } from './reservation/reservation.component';
import { RoomTypeComponent } from './room-type/room-type.component';
import { RoomsComponent } from './rooms/rooms.component';

const routes: Routes = [
  { path:'login', component: LoginComponent },
  { path:'register', component: RegisterComponent },
  { path:'home', component: HomeComponent },
  { path: 'guests', component: GuestListComponent },
  { path: 'guests/:id', component: GuestListComponent },
  { path: 'reservations', component: ReservationComponent},
  { path: 'reservations/:id', component: ReservationComponent},
  { path: 'roomtypes', component: RoomTypeComponent},
  { path: 'rooms', component: RoomsComponent},
  { path: '', redirectTo: '/login', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
