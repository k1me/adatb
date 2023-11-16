import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { finalize, tap, catchError } from 'rxjs/operators';
import { of } from 'rxjs';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  felhasznalonev: string = '';
  jelszo: string = '';
  isLoading: boolean = false;

  constructor(private http: HttpClient, private router: Router) { }

  register() {
    this.router.navigate(['/register']);
  }

  async login() {
    const credentials = { felhasznalonev: this.felhasznalonev, jelszo: this.jelszo };
    this.isLoading = true;

    this.http.post<any>('http://localhost:8000/felhasznalo/login', credentials, {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }).pipe(
      tap(response => {
        console.log('Login successful');
        localStorage.setItem('token', response.token);
        this.router.navigate(['/home']);
      }),
      catchError(error => {
        console.error('Login failed', error);
        return of(null); 
      }),
      finalize(() => {
        this.isLoading = false;
      })
    ).subscribe();


  }
}
