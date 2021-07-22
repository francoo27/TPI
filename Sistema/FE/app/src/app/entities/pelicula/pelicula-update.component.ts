import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { PeliculaService } from './pelicula.service';
import { IPelicula } from './pelicula.model';
import { MessageService } from 'primeng/api';
import { Location } from '@angular/common';
import { ClasificacionService } from '../clasifiacion/clasificacion.service';
import { IClasificacion } from '../clasifiacion/clasificacion.model';
import { IGenero } from '../genero/genero.model';
import { GeneroService } from '../genero/genero.service';
import { PaisService } from '../pais/pais.service';
import { IPais } from '../pais/pais.model';
import { IFormato } from '../formato/formato.model';
import { FormatoService } from '../formato/formato.service';
import {formatDate} from '@angular/common';
import { DATE_FORMAT } from 'src/app/shared/dateFormat';
import { DateTime } from "luxon";


@Component({
    selector: 'car-pelicula-update',
    templateUrl: './pelicula-update.component.html'
})
export class PeliculaUpdateComponent implements OnInit {
    private _pelicula!: IPelicula;
    clasificaciones:IClasificacion[]=[];
    generos:IGenero[]=[];
    paises:IPais[]=[];
    formatos:IFormato[]=[];
    currentNombre!: string;
    fechaEstreno!: Date;
    fechaEstrenoFormat!: DateTime;
    isSaving!: boolean;
    uploadedFiles:any[]=[];
    canUpload!: boolean;

    constructor(
        private peliculaService: PeliculaService,
        private clasificacionService: ClasificacionService,
        private generoService: GeneroService,
        private paisService: PaisService,
        private formatoService: FormatoService,
        private activatedRoute: ActivatedRoute,
        private messageService: MessageService,
        private location: Location
    ) {}

    ngOnInit() {
        this.isSaving = false;
        this.canUpload = true;

        this.activatedRoute.data.subscribe(({ pelicula }) => {
            this.pelicula = pelicula;
            this.currentNombre = pelicula.tituloPais;


            var date = new Date(pelicula.fechaEstreno)
            var userTimezoneOffset = date.getTimezoneOffset() * 60000;
            this.fechaEstreno = new Date(date.getTime() - userTimezoneOffset);
            this.canUpload = this.pelicula.imagen != null  || this.pelicula.imagen != undefined ? false : true;
        });


        if (this.isNew()){
            this.fechaEstreno = new Date()
        }

        this.clasificacionService.query().subscribe(res => {
            this.clasificaciones = res.body!
        } )

        this.generoService.query().subscribe(res => {
            this.generos = res.body!
        } )

        this.paisService.query().subscribe(res => {
            this.paises = res.body!
        } )
        
        this.formatoService.query().subscribe(res => {
            this.formatos = res.body!
        } )
    }

    previousState() {
        this.location.back();
    }

    onSubmit(){
        console.log("asds")
    }
    onUpload($event:any){
        for(let file of $event.files) {
            this.canUpload = false;
            this.uploadedFiles.push(file);
            this.pelicula.imagen = file.name
            console.log(this.canUpload);
        }
        console.log($event);
    }

    save() {
        this.isSaving = true;
        this.pelicula.fechaEstreno = DateTime.fromJSDate(this.fechaEstreno).toFormat(DATE_FORMAT)
        if (this.isNew()) {
            this.subscribeToSaveResponse(this.peliculaService.create(this.pelicula));
        } else {
            this.subscribeToSaveResponse(this.peliculaService.update(this.pelicula));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<IPelicula>>) {
        result.subscribe(() => this.onSaveSuccess(), () => this.onSaveError());
    }

    isNew() {
        return this.pelicula.id === undefined;
    }

    private onSaveSuccess() {
        this.isSaving = false;
        setTimeout(() => {
            this.messageService.add({
                severity: "success",
                summary: "Todo Ok!",
                detail: this.isNew() ? "Pelicula creada":"Pelicula editada"
            })
        }, 1000);
        this.previousState();
    }

    private onSaveError() {
        setTimeout(() => {
            this.messageService.add({
                severity: "error",
                summary: "ERROR",
                detail: this.isNew() ? "Hubo un error al crear el Pelicula":"Hubo un error al editar el Pelicula"
            });
        }, 1000);
        this.isSaving = false;
    }

    get pelicula() {
        return this._pelicula;
    }

    set pelicula(pelicula: IPelicula) {
        this._pelicula = pelicula;
    }
}
