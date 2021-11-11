import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api/menuitem';
import { AuthService } from './auth.service';
import { Location } from '@angular/common';
@Component({
  selector: 'login',
  templateUrl: './login.component.html'
  ,providers: []
})
export class LoginComponent implements OnInit {
    loggin:boolean = false;
    password!:string;
    email!:string;

    constructor(
      private authService: AuthService,
      private location: Location
  ) {
  }

    ngOnInit(){
      // localStorage.setItem('token', 'Como utilizar el LocalStorage en Angular');
      // console.log(localStorage.getItem('token'))
    }

    login(){
      this.authService.login({email:this.email,password:this.password}).subscribe(
        res => {
          localStorage.setItem('token', res.body?.token!)
          localStorage.setItem('email', this.email!)
          this.authService.authenticate({token:localStorage.getItem('token')!}).subscribe(
            res => console.log(res.body),
            err => console.log(err),
            () =>  this.location.back()
          )
          }
        )

    }
    previousState() {
      this.location.back();
  }
}

