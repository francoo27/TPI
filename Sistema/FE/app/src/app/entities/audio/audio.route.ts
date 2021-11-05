import { Injectable } from '@angular/core';
import { HttpResponse } from '@angular/common/http';
import { Resolve, ActivatedRouteSnapshot, Routes } from '@angular/router';
import { of } from 'rxjs';
import { map } from 'rxjs/operators';
import { AudioUpdateComponent } from './audio-update.component';
import { IAudio, Audio } from './audio.model';
import { AudioService } from './audio.service';
import { AudioComponent } from './audio.component';

@Injectable({ providedIn: 'root' })
export class AudioResolve implements Resolve<IAudio> {
    constructor(private audioService: AudioService) {}

    resolve(route: ActivatedRouteSnapshot) {
        const id = route.params['id'] ? route.params['id'] : null;

        return id
            ? this.audioService.find(id).pipe(map((res: HttpResponse<IAudio>) => res.body!))
            : of(new Audio());
    }
}

export const audioRoute: Routes = [
    {
        path: '',
        component: AudioComponent
    },
    {
        path: ':id/edit',
        component: AudioUpdateComponent,
        resolve: {
            audio: AudioResolve
        },
        data: {
            pageTitle: 'Audio'
        }
    },
    {
        path: 'new',
        component: AudioUpdateComponent,
        resolve: {
            audio: AudioResolve
        },
        data: {
            pageTitle: 'Audio'
        }
    },
];
