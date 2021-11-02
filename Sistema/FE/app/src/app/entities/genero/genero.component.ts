import { Component, OnInit, OnDestroy } from '@angular/core';
import {MessageService} from 'primeng/api';
import { IGenero } from './genero.model';
import { GeneroService } from './genero.service';

@Component({
    selector: 'car-genero',
    templateUrl: './genero.component.html',
    providers: []
})
export class GeneroComponent implements OnInit, OnDestroy {
    generos: IGenero[] =  [];

    constructor(
        private generoService: GeneroService,
        private messageService: MessageService
    ) {
    }

    ngOnInit(): void {
      this.generoService.query().subscribe(res => {
        this.generos = res.body!
    } );

    }

    delete(id:number):void{
        this.generoService.delete(id).subscribe(
            x => {
                setTimeout(() => {
                    this.messageService.add({
                        severity: "success",
                        summary: "Todo Ok!",
                        detail:"Genero Eliminado"
                    })
                }, 100);
            },
            res => {
                setTimeout(() => {
                    this.messageService.add({
                        severity: "error",
                        summary: "ERROR",
                        detail:res.error.message
                    })
                }, 100);
            },
            () => {
                this.generoService.query().subscribe(res => {
                    this.generos = res.body!
                });
            }
        );
    }

    ngOnDestroy(): void {}
}
