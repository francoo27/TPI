import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { FuncionService } from './funcion.service';
import { IFuncion } from './funcion.model';
import { MessageService } from 'primeng/api';
import { Location } from '@angular/common';
import { IFormato } from '../formato/formato.model';
import { FormatoService } from '../formato/formato.service';
import { IPelicula } from '../pelicula/pelicula.model';
import { PeliculaService } from '../pelicula/pelicula.service';
import { ISala } from '../sala/sala.model';
import { IComplejo } from '../complejo/complejo.model';
import { ComplejoService } from '../complejo/complejo.service';
import { SalaService } from '../sala/sala.service';


@Component({
    selector: 'car-funcion-update',
    templateUrl: './funcion-update.component.html'
})
export class FuncionUpdateComponent implements OnInit {
    private _funcion!: IFuncion;

    formatos:IFormato[]=[];
    peliculas:IPelicula[]=[];
    complejos:IComplejo[]=[];
    salas:ISala[]=[];

    complejo!:IComplejo;

    currentNombre!: string;
    isSaving!: boolean;

    fecha!: Date;

    hora!: Date
    minFecha: Date = new Date();

    constructor(
        private funcionService: FuncionService,
        private complejoService: ComplejoService,
        private peliculaService: PeliculaService,
        private salaService: SalaService,
        private activatedRoute: ActivatedRoute,
        private messageService: MessageService,
        private location: Location
    ) {}

    ngOnInit() {
        this.isSaving = false;

        this.activatedRoute.data.subscribe(({ funcion }) => {
            this.funcion = funcion;
            this.currentNombre = funcion.nombre;
        });

        this.complejoService.query().subscribe(res => {
            this.complejos = res.body!
        } )

        this.peliculaService.query().subscribe(res => {
            this.peliculas = res.body!
        } )


    }

    previousState() {
        this.location.back();
    }

    onSubmit(){
        console.log("asds")
    }

    generateNombre(){
        return `${this.funcion.pelicula && this.funcion.formato 
            ? this.funcion.pelicula?.tituloPais! + " - " + this.funcion.formato?.nombre! + " - " + "Sala: " + this.funcion.sala?.numero! + " - " + (this.fecha ? this.fecha!.getDate().toString()+"/"+this.fecha!.getMonth().toString() : "") + " - " + (this.hora ? this.hora!.getHours().toString() + ":" + this.hora!.getMinutes().toString(): "") 
            : ""}`;
    }

    onComplejoChange(){
        this.salaService.query_ByComplejo(this.complejo.id!).subscribe(res => {
            this.salas = res.body!
        } )
    }

    onSalaChange(){
        this.formatos=this.funcion.sala?.formatos!;
    }

    save() {
        this.isSaving = true;
        if (this.isNew()) {
            this.subscribeToSaveResponse(this.funcionService.create(this.funcion));
        } else {
            this.subscribeToSaveResponse(this.funcionService.update(this.funcion));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<IFuncion>>) {
        result.subscribe(() => this.onSaveSuccess(), () => this.onSaveError());
    }

    isNew() {
        return this.funcion.id === undefined;
    }

    private onSaveSuccess() {
        this.isSaving = false;
        setTimeout(() => {
            this.messageService.add({
                severity: "success",
                summary: "Ok!",
                detail: this.isNew() ? "Funcion creada":"Funcion editada"
            })
        }, 1000);
        this.previousState();
    }

    private onSaveError() {
        setTimeout(() => {
            this.messageService.add({
                severity: "error",
                summary: "ERROR",
                detail: this.isNew() ? "Hubo un error al crear el Funcion":"Hubo un error al editar el Funcion"
            })
        }, 1000);
        this.isSaving = false;
    }

    get funcion() {
        return this._funcion;
    }

    set funcion(funcion: IFuncion) {
        this._funcion = funcion;
    }
}
