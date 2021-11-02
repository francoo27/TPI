import { Component, OnInit, OnDestroy } from '@angular/core';
import {MessageService} from 'primeng/api';
import { IClasificacion } from './clasificacion.model';
import { ClasificacionService } from './clasificacion.service';

@Component({
    selector: 'car-clasificacion',
    templateUrl: './clasificacion.component.html',
    providers: []
})
export class ClasificacionComponent implements OnInit, OnDestroy {
    clasificacions: IClasificacion[] =  [];

    constructor(
        private clasificacionService: ClasificacionService,
        private messageService: MessageService
    ) {
    }

    ngOnInit(): void {
      this.clasificacionService.query().subscribe(res => {
        this.clasificacions = res.body!
    } );

    }

    delete(id:number):void{
        this.clasificacionService.delete(id).subscribe(
            x => {
                setTimeout(() => {
                    this.messageService.add({
                        severity: "success",
                        summary: "Todo Ok!",
                        detail:"Clasificacion Eliminada"
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
                this.clasificacionService.query().subscribe(res => {
                    this.clasificacions = res.body!
                });
            }
        );
    }

    ngOnDestroy(): void {}
}
