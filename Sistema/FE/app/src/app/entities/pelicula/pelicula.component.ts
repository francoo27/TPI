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
        });
    }

    delete(id:number):void{
        console.log(id)
        this.peliculaService.delete(id).subscribe(
            x => {
                setTimeout(() => {
                    this.messageService.add({
                        severity: "success",
                        summary: "Todo Ok!",
                        detail:"Pelicula Eliminada"
                    })
                }, 100);
            },
            err => {
                setTimeout(() => {
                    this.messageService.add({
                        severity: "error",
                        summary: "ERROR",
                        detail:"Error al eliminar pelicula"
                    })
                }, 100);
            },
            () => {
                this.peliculaService.query().subscribe(res => {
                    this.peliculas = res.body!
                });
            }
        );
    }

    ngOnDestroy(): void {}
}
