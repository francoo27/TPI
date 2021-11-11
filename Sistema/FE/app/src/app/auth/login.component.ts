import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api/menuitem';

@Component({
  selector: 'login',
  templateUrl: './login.component.html'
  ,providers: []
})
export class LoginComponent implements OnInit {
    loggin:boolean = false;
    password!:string;
    email!:string;

    ngOnInit(){
      localStorage.setItem('token', 'Como utilizar el LocalStorage en Angular');
      console.log(localStorage.getItem('token'))
    }
    login(){
      console.log(localStorage.getItem('token'))
    }
}

