import { Injectable } from '@angular/core';
import { HttpResponse } from '@angular/common/http';
import { Resolve, ActivatedRouteSnapshot, Routes } from '@angular/router';
import { of } from 'rxjs';
import { map } from 'rxjs/operators';
import { ClasificacionUpdateComponent } from './clasificacion-update.component';
import { IClasificacion, Clasificacion } from './clasificacion.model';
import { ClasificacionService } from './clasificacion.service';
import { ClasificacionComponent } from './clasificacion.component';

@Injectable({ providedIn: 'root' })
export class ClasificacionResolve implements Resolve<IClasificacion> {
    constructor(private clasificacionService: ClasificacionService) {}

    resolve(route: ActivatedRouteSnapshot) {
        const id = route.params['id'] ? route.params['id'] : null;

        return id
            ? this.clasificacionService.find(id).pipe(map((res: HttpResponse<IClasificacion>) => res.body!))
            : of(new Clasificacion());
    }
}

export const clasificacionRoute: Routes = [
    {
        path: '',
        component: ClasificacionComponent
    },
    {
        path: ':id/edit',
        component: ClasificacionUpdateComponent,
        resolve: {
            clasificacion: ClasificacionResolve
        },
        data: {
            pageTitle: 'Clasificacion'
        }
    },
    {
        path: 'new',
        component: ClasificacionUpdateComponent,
        resolve: {
            clasificacion: ClasificacionResolve
        },
        data: {
            pageTitle: 'Clasificacion'
        }
    },
];
