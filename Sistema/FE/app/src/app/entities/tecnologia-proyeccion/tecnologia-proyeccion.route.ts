import { Injectable } from '@angular/core';
import { HttpResponse } from '@angular/common/http';
import { Resolve, ActivatedRouteSnapshot, Routes } from '@angular/router';
import { of } from 'rxjs';
import { map } from 'rxjs/operators';
import { TecnologiaProyeccionUpdateComponent } from './tecnologia-proyeccion-update.component';
import { ITecnologiaProyeccion, TecnologiaProyeccion } from './tecnologia-proyeccion.model';
import { TecnologiaProyeccionService } from './tecnologia-proyeccion.service';
import { TecnologiaProyeccionComponent } from './tecnologia-proyeccion.component';

@Injectable({ providedIn: 'root' })
export class TecnologiaProyeccionResolve implements Resolve<ITecnologiaProyeccion> {
    constructor(private tecnologiaProyeccionService: TecnologiaProyeccionService) {}

    resolve(route: ActivatedRouteSnapshot) {
        const id = route.params['id'] ? route.params['id'] : null;

        return id
            ? this.tecnologiaProyeccionService.find(id).pipe(map((res: HttpResponse<ITecnologiaProyeccion>) => res.body!))
            : of(new TecnologiaProyeccion());
    }
}

export const tecnologiaProyeccionRoute: Routes = [
    {
        path: '',
        component: TecnologiaProyeccionComponent
    },
    {
        path: ':id/edit',
        component: TecnologiaProyeccionUpdateComponent,
        resolve: {
            tecnologiaProyeccion: TecnologiaProyeccionResolve
        },
        data: {
            pageTitle: 'TecnologiaProyeccion'
        }
    },
    {
        path: 'new',
        component: TecnologiaProyeccionUpdateComponent,
        resolve: {
            tecnologiaProyeccion: TecnologiaProyeccionResolve
        },
        data: {
            pageTitle: 'TecnologiaProyeccion'
        }
    },
];
