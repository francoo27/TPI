import { Routes } from '@angular/router';
import { LoginComponent } from './login.component';


export const authRoute: Routes = [
    {
        path: 'login',
        component: LoginComponent,
        data: {
            pageTitle: 'Login'
        }
    },
];
