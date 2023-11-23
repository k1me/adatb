import { Component } from '@angular/core';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';
import { tap } from 'rxjs';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent {
  felhasznalo: any = {};
  confirmPassword: string = '';

  constructor(private authService: AuthService, private router: Router) { }

  async register() {
    if (this.felhasznalo.jelszo !== this.confirmPassword) {
      console.error('A két jelszó nem egyezik meg.');
      return;
    }

    this.authService.register(this.felhasznalo).pipe(
      tap({
        next: response => {
          console.log('Sikeres regisztráció', response);
          this.router.navigate(['/login']);
        },
        error: error => {
          console.error('Sikertelen regisztráció', error);
        }
      })
    ).subscribe();
  }
}