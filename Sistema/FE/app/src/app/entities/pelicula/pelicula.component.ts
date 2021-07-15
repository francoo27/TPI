import { Component, OnInit, OnDestroy } from '@angular/core';
import {MessageService} from 'primeng/api';
import { PeliculaService } from './pelicula.service';

@Component({
    selector: 'car-pelicula',
    templateUrl: './pelicula.component.html',
    providers: []
})
export class PeliculaComponent implements OnInit, OnDestroy {
    peliculas: any[] =  [{
        name: 'Australia',
        code: 'AU'
    }];
    selectedCity1: any;


    constructor(
        private peliculaService: PeliculaService,
        private messageService: MessageService
    ) {
    }

    ngOnInit(): void {
      this.peliculaService.query().subscribe(res => {
        this.peliculas = res.body!
    } );

    }

    ngOnDestroy(): void {}
}
