import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { tap } from 'rxjs/operators';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {

  felhasznalonev: string = '';
  jelszo: string = '';

  constructor(private authService: AuthService, private router: Router) { }

  register() {
    this.router.navigate(['/register']);
  }

  async login() {
    this.authService.login({ felhasznalonev: this.felhasznalonev, jelszo: this.jelszo })
      .pipe(
        tap(response => {
          sessionStorage.setItem('loginToken', response.felhasznalonev);
          this.router.navigate(['/home']);
        })
      )
      .subscribe();
  }
}
