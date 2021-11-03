import { Routes } from '@angular/router';
import { PeliculaResolve } from '../pelicula/pelicula.route';
import { BoleteriaComponent } from './boleteria.component';



export const boleteriaRoute: Routes = [
    {
        path: '',
        component: BoleteriaComponent,
        data: {
            pageTitle: 'CineAr'
        }
    },
    {
        path: ':id',
        resolve: {
            pelicula: PeliculaResolve
        },
        component: BoleteriaComponent,
        data: {
            pageTitle: 'CineAr'
        }
    }
];
