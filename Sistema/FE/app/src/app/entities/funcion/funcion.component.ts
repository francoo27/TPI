import { Component, OnInit, OnDestroy } from '@angular/core';
import {MessageService} from 'primeng/api';
import { IFuncion } from './funcion.model';
import { FuncionService } from './funcion.service';

@Component({
    selector: 'car-funcion',
    templateUrl: './funcion.component.html',
    providers: []
})
export class FuncionComponent implements OnInit, OnDestroy {
    funciones: IFuncion[] =  [];
    selectedCity1: any;


    constructor(
        private funcionService: FuncionService,
        private messageService: MessageService
    ) {
    }

    ngOnInit(): void {
      this.funcionService.query().subscribe(res => {
        this.funciones = res.body!
    } );

    }

    cancel(id:number):void{
        this.funcionService.cancel(id).subscribe(
            x => {
                setTimeout(() => {
                    this.messageService.add({
                        severity: "success",
                        summary: "Todo Ok!",
                        detail:"Funcion Cancelada"
                    })
                }, 100);
            },
            res => {
                setTimeout(() => {
                    this.messageService.add({
                        severity: "error",
                        summary: "ERROR",
                        detail:"No es posible cancelar esta Funcion"
                    })
                }, 100);
            },
            () => {
                this.funcionService.query().subscribe(res => {
                    this.funciones = res.body!
                });
            }
        );
    }

    delete(id:number):void{
        this.funcionService.delete(id).subscribe(
            x => {
                setTimeout(() => {
                    this.messageService.add({
                        severity: "success",
                        summary: "Todo Ok!",
                        detail:"Funcion Eliminado"
                    })
                }, 100);
            },
            res => {
                setTimeout(() => {
                    this.messageService.add({
                        severity: "error",
                        summary: "ERROR",
                        detail:"No es posible eliminar esta Funcion"
                    })
                }, 100);
            },
            () => {
                this.funcionService.query().subscribe(res => {
                    this.funciones = res.body!
                });
            }
        );
    }

    ngOnDestroy(): void {}
}
