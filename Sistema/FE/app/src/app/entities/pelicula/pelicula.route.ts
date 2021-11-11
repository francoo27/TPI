import { Injectable } from '@angular/core';
import { HttpResponse } from '@angular/common/http';
import { Resolve, ActivatedRouteSnapshot, Routes } from '@angular/router';
import { of } from 'rxjs';
import { map } from 'rxjs/operators';
import { PeliculaUpdateComponent } from './pelicula-update.component';
import { IPelicula, Pelicula } from './pelicula.model';
import { PeliculaService } from './pelicula.service';
import { PeliculaDetailComponent } from './pelicula-detail.component';
import { PeliculaComponent } from './pelicula.component';
import { CanActivateAuth} from '../../auth/canActivateAuth'

@Injectable({ providedIn: 'root' })
export class PeliculaResolve implements Resolve<IPelicula> {
    constructor(private peliculaService: PeliculaService) {}

    resolve(route: ActivatedRouteSnapshot) {
        const id = route.params['id'] ? route.params['id'] : null;

        return id
            ? this.peliculaService.find(id).pipe(map((res: HttpResponse<IPelicula>) => res.body!))
            : of(new Pelicula());
    }
}

export const peliculaRoute: Routes = [
    {
        path: '',
        component: PeliculaComponent,
        canActivate:[CanActivateAuth]
    },
    {
        path: ':id/view',
        component: PeliculaDetailComponent,
        resolve: {
            pelicula: PeliculaResolve
        },
        data: {
            pageTitle: 'Pelicula'
        },
        canActivate:[CanActivateAuth]
    },
    {
        path: ':id/edit',
        component: PeliculaUpdateComponent,
        resolve: {
            pelicula: PeliculaResolve
        },
        data: {
            pageTitle: 'Pelicula'
        }
    },
    {
        path: 'new',
        component: PeliculaUpdateComponent,
        resolve: {
            pelicula: PeliculaResolve
        },
        data: {
            pageTitle: 'Pelicula'
        }
    },
];
