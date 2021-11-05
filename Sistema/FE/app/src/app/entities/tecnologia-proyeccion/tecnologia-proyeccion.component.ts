import { Component, OnInit, OnDestroy } from '@angular/core';
import {MessageService} from 'primeng/api';
import { ITecnologiaProyeccion } from './tecnologia-proyeccion.model';
import { TecnologiaProyeccionService } from './tecnologia-proyeccion.service';

@Component({
    selector: 'car-tecnologia-proyeccion',
    templateUrl: './tecnologia-proyeccion.component.html',
    providers: []
})
export class TecnologiaProyeccionComponent implements OnInit, OnDestroy {
    tecnologiaProyeccions: ITecnologiaProyeccion[] =  [];

    constructor(
        private tecnologiaProyeccionService: TecnologiaProyeccionService,
        private messageService: MessageService
    ) {
    }

    ngOnInit(): void {
      this.tecnologiaProyeccionService.query().subscribe(res => {
        this.tecnologiaProyeccions = res.body!
    } );

    }

    delete(id:number):void{
        this.tecnologiaProyeccionService.delete(id).subscribe(
            x => {
                setTimeout(() => {
                    this.messageService.add({
                        severity: "success",
                        summary: "Todo Ok!",
                        detail:"Tecnologia Proyeccion Eliminada"
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
                this.tecnologiaProyeccionService.query().subscribe(res => {
                    this.tecnologiaProyeccions = res.body!
                });
            }
        );
    }

    ngOnDestroy(): void {}
}
