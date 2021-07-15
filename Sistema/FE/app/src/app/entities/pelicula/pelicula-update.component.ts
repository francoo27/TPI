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


@Component({
    selector: 'car-pelicula-update',
    templateUrl: './pelicula-update.component.html'
})
export class PeliculaUpdateComponent implements OnInit {
    private _pelicula!: IPelicula;
    clasificaciones:IClasificacion[]=[];
    generos:IGenero[]=[];
    currentNombre!: string;
    isSaving!: boolean;

    constructor(
        private peliculaService: PeliculaService,
        private clasificacionService: ClasificacionService,
        private generoService: GeneroService,
        private activatedRoute: ActivatedRoute,
        private messageService: MessageService,
        private location: Location
    ) {}

    ngOnInit() {
        this.isSaving = false;

        this.activatedRoute.data.subscribe(({ pelicula }) => {
            this.pelicula = pelicula;
            this.currentNombre = pelicula.nombre;
        });

        this.clasificacionService.query().subscribe(res => {
            this.clasificaciones = res.body!
        } )

        this.clasificacionService.query().subscribe(res => {
            this.generos = res.body!
        } )
    }

    previousState() {
        this.location.back();
    }

    onSubmit(){
        console.log("asds")
    }
    onUpload($event:any){

    }

    save() {
        this.isSaving = true;
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
        this.messageService.add({
            severity: "success",
            summary: "Ok!",
            detail: this.isNew() ? "Pelicula creado":"Pelicula editado"
          });
        this.previousState();
    }

    private onSaveError() {
        this.messageService.add({
            severity: "error",
            summary: "Ok!",
            detail: this.isNew() ? "Hubo un error al crear el Pelicula":"Hubo un error al editar el Pelicula"
          });
        this.isSaving = false;
    }

    get pelicula() {
        return this._pelicula;
    }

    set pelicula(motivo: IPelicula) {
        this._pelicula = motivo;
    }
}
