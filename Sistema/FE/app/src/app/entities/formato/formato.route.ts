import { Injectable } from '@angular/core';
import { HttpResponse } from '@angular/common/http';
import { Resolve, ActivatedRouteSnapshot, Routes } from '@angular/router';
import { of } from 'rxjs';
import { map } from 'rxjs/operators';
import { FormatoUpdateComponent } from './formato-update.component';
import { IFormato, Formato } from './formato.model';
import { FormatoService } from './formato.service';
import { FormatoComponent } from './formato.component';

@Injectable({ providedIn: 'root' })
export class FormatoResolve implements Resolve<IFormato> {
    constructor(private formatoService: FormatoService) {}

    resolve(route: ActivatedRouteSnapshot) {
        const id = route.params['id'] ? route.params['id'] : null;

        return id
            ? this.formatoService.find(id).pipe(map((res: HttpResponse<IFormato>) => res.body!))
            : of(new Formato());
    }
}

export const formatoRoute: Routes = [
    {
        path: '',
        component: FormatoComponent
    },
    {
        path: ':id/edit',
        component: FormatoUpdateComponent,
        resolve: {
            formato: FormatoResolve
        },
        data: {
            pageTitle: 'Formato'
        }
    },
    {
        path: 'new',
        component: FormatoUpdateComponent,
        resolve: {
            formato: FormatoResolve
        },
        data: {
            pageTitle: 'Formato'
        }
    },
];
