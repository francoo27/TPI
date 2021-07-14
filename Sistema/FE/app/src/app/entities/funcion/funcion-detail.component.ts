import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { IFuncion } from './funcion.model';

@Component({
    selector: 'car-funcion-detail',
    templateUrl: './funcion-detail.component.html'
})
export class FuncionDetailComponent implements OnInit {
    funcion!: IFuncion;

    constructor(private activatedRoute: ActivatedRoute) {}

    ngOnInit(): void {
        this.activatedRoute.data.subscribe(({ funcion }) => this.funcion = funcion);
    }
}
