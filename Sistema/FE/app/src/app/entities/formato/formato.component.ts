import { Component, OnInit, OnDestroy } from '@angular/core';
import {MessageService} from 'primeng/api';
import { IFormato } from './formato.model';
import { FormatoService } from './formato.service';

@Component({
    selector: 'car-formato',
    templateUrl: './formato.component.html',
    providers: []
})
export class FormatoComponent implements OnInit, OnDestroy {
    formatos: IFormato[] =  [];

    constructor(
        private formatoService: FormatoService,
        private messageService: MessageService
    ) {
    }

    ngOnInit(): void {
      this.formatoService.query().subscribe(res => {
        this.formatos = res.body!
    } );

    }

    delete(id:number):void{
        this.formatoService.delete(id).subscribe(
            x => {
                setTimeout(() => {
                    this.messageService.add({
                        severity: "success",
                        summary: "Todo Ok!",
                        detail:"Formato Eliminado"
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
                this.formatoService.query().subscribe(res => {
                    this.formatos = res.body!
                });
            }
        );
    }

    ngOnDestroy(): void {}
}
