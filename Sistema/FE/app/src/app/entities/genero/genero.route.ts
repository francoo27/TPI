import { Injectable } from '@angular/core';
import { HttpResponse } from '@angular/common/http';
import { Resolve, ActivatedRouteSnapshot, Routes } from '@angular/router';
import { of } from 'rxjs';
import { map } from 'rxjs/operators';
import { GeneroUpdateComponent } from './genero-update.component';
import { IGenero, Genero } from './genero.model';
import { GeneroService } from './genero.service';
import { GeneroComponent } from './genero.component';

@Injectable({ providedIn: 'root' })
export class GeneroResolve implements Resolve<IGenero> {
    constructor(private generoService: GeneroService) {}

    resolve(route: ActivatedRouteSnapshot) {
        const id = route.params['id'] ? route.params['id'] : null;

        return id
            ? this.generoService.find(id).pipe(map((res: HttpResponse<IGenero>) => res.body!))
            : of(new Genero());
    }
}

export const generoRoute: Routes = [
    {
        path: '',
        component: GeneroComponent
    },
    {
        path: ':id/edit',
        component: GeneroUpdateComponent,
        resolve: {
            genero: GeneroResolve
        },
        data: {
            pageTitle: 'Genero'
        }
    },
    {
        path: 'new',
        component: GeneroUpdateComponent,
        resolve: {
            genero: GeneroResolve
        },
        data: {
            pageTitle: 'Genero'
        }
    },
];
