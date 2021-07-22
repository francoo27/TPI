import { Routes } from '@angular/router';
import { BoleteriaComponent } from './boleteria.component';



export const boleteriaRoute: Routes = [
    {
        path: '',
        component: BoleteriaComponent,
        data: {
            pageTitle: 'CineAr'
        }
    }
];
