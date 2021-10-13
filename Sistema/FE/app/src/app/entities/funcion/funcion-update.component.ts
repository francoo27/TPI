import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { FuncionService } from './funcion.service';
import { Funcion, FuncionCreate, IFuncion, IFuncionCreate, mapToFuncionCreate } from './funcion.model';
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
import { formatDate } from 'src/app/shared/dateFormat';


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


    salaSelected!:ISala;
    peliculaSelected!:IPelicula;
    complejoSelected!:IComplejo;
    formatoSelected!:IFormato;

    currentNombre!: string;
    isSaving!: boolean;

    fecha!: Date;
    fechaStr!: string;

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

        this.activatedRoute.data.subscribe( ( res ) => {
            this.funcion = res.funcion;
            this.currentNombre = res.funcion.nombre!;
            this.complejoSelected = res.funcion.sala.complejo!;
            this.fecha = new Date(res.funcion.fechaInicio!);
            console.log(this.funcion)
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
        let fecha = new Date(Date.parse(this.fechaStr));
        this.funcion.nombre = 
         `${this.funcion.pelicula?.id && this.funcion.formato?.id 
            ? this.funcion.pelicula?.tituloPais! + " - " + this.funcion.formato?.nombre! + " - " + "Sala: " + this.funcion.sala?.numero! + " - " + (fecha ? fecha!.getDate().toString()+"/"+ (fecha!.getMonth()+1).toString() : "") + " - " + (this.hora ? this.hora!.getHours().toString() + ":" + this.hora!.getMinutes().toString(): "") 
            : ""}`;
        return this.funcion.nombre;
    }

    onComplejoChange(){
        this.salaService.query_ByComplejo(this.complejoSelected.id!).subscribe(res => {
            this.salas = res.body!
            this.funcion.sala = this.funcion.sala;
        } )
    }

    onSalaChange(){
        // this.formatos=this.funcion.sala?.formatos!;
        this.formatos = [];
        let formatosDisp = this.funcion.sala?.formatos!.map(x => {
            let item = this.funcion.pelicula?.formatos!.find(item => item.id === x.id);
            return item!;
          }).filter(item => item !== undefined)!;
        this.formatos = formatosDisp !== undefined && formatosDisp!.length > 0 ? formatosDisp : this.formatos! ;
        //this.funcion.salaId = this.salaSelected.id;
    }

    save() {
        this.isSaving = true;
        this.funcion.horaInicio = this.hora.toString();
        let saveFuncion = mapToFuncionCreate(this.funcion);
        let saveDate = new Date(Date.parse(this.fechaStr));
        saveFuncion.fechaAnio = saveDate.getFullYear();
        saveFuncion.fechaMes = saveDate.getMonth()+1;
        saveFuncion.fechaDia = saveDate.getDate();
        saveFuncion.hora = Number(new Date(this.hora).getHours());
        saveFuncion.minuto = Number(new Date(this.hora).getMinutes());
        if (this.isNew()) {
            this.subscribeToSaveResponse(this.funcionService.create(saveFuncion));
        } else {
            this.subscribeToSaveResponse(this.funcionService.update(saveFuncion));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<IFuncionCreate>>) {
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

    get funcion():IFuncion {
        return this._funcion;
    }

    set funcion(funcion: IFuncion) {
        this._funcion =  funcion;
    }
}
