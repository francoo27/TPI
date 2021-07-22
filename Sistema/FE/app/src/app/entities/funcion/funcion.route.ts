import { Injectable } from '@angular/core';
import { HttpResponse } from '@angular/common/http';
import { Resolve, ActivatedRouteSnapshot, Routes } from '@angular/router';
import { of } from 'rxjs';
import { map } from 'rxjs/operators';
import { FuncionUpdateComponent } from './funcion-update.component';
import { IFuncion, Funcion } from './funcion.model';
import { FuncionService } from './funcion.service';
import { FuncionDetailComponent } from './funcion-detail.component';
import { FuncionComponent } from './funcion.component';

@Injectable({ providedIn: 'root' })
export class FuncionResolve implements Resolve<IFuncion> {
    constructor(private funcionService: FuncionService) {}

    resolve(route: ActivatedRouteSnapshot) {
        const id = route.params['id'] ? route.params['id'] : null;

        return id
            ? this.funcionService.find(id).pipe(map((res: HttpResponse<IFuncion>) => res.body!))
            : of(new Funcion());
    }
}

export const funcionRoute: Routes = [
    {
        path: '',
        component: FuncionComponent
    },
    {
        path: ':id/view',
        component: FuncionDetailComponent,
        resolve: {
            funcion: FuncionResolve
        },
        data: {
            pageTitle: 'Funcion'
        }
    },
    {
        path: ':id/edit',
        component: FuncionUpdateComponent,
        resolve: {
            funcion: FuncionResolve
        },
        data: {
            pageTitle: 'Funcion'
        }
    },
    {
        path: 'new',
        component: FuncionUpdateComponent,
        resolve: {
            funcion: FuncionResolve
        },
        data: {
            pageTitle: 'Funcion'
        }
    },
];
