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

    ngOnDestroy(): void {}
}
