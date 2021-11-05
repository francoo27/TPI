import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { FormatoService } from './formato.service';
import { IFormato } from './formato.model';
import { MessageService } from 'primeng/api';
import { Location } from '@angular/common';
import { IAudio } from '../audio/audio.model';
import { ITecnologiaProyeccion } from '../tecnologia-proyeccion/tecnologia-proyeccion.model';
import { AudioService } from '../audio/audio.service';
import { TecnologiaProyeccionService } from '../tecnologia-proyeccion/tecnologia-proyeccion.service';


@Component({
    selector: 'car-formato-update',
    templateUrl: './formato-update.component.html'
})
export class FormatoUpdateComponent implements OnInit {
    private _formato!: IFormato;
    currentNombre!: string;
    audio!: IAudio;
    tecnologiaProyeccion!: ITecnologiaProyeccion;
    isSaving!: boolean;

    audios:IAudio[]=[];
    tecnologiasProyeccion:ITecnologiaProyeccion[]=[];


    constructor(
        private formatoService: FormatoService,
        private activatedRoute: ActivatedRoute,
        private messageService: MessageService,
        private location: Location,
        private audioService: AudioService,
        private tecnologiaProyeccionService: TecnologiaProyeccionService
    ) {}

    ngOnInit() {
        this.isSaving = false;

        this.activatedRoute.data.subscribe(({ formato }) => {
            this.formato = formato;
            this.currentNombre = formato.nombre;
        });

        this.audioService.query().subscribe(res => {
            this.audios = res.body!
        } )

        this.tecnologiaProyeccionService.query().subscribe(res => {
            this.tecnologiasProyeccion = res.body!
        } )
    }

    previousState() {
        this.location.back();
    }

    changeNombre(){
        this.formato.nombre = this.audio == undefined || this.tecnologiaProyeccion == undefined ? "" : this.tecnologiaProyeccion.nombre + " " + this.audio.nombre; 
    }

    save() {
        this.isSaving = true;
        if (this.isNew()) {
            this.subscribeToSaveResponse(this.formatoService.create(this.formato));
        } else {
            this.subscribeToSaveResponse(this.formatoService.update(this.formato));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<IFormato>>) {
        result.subscribe(() => this.onSaveSuccess(), (x) => this.onSaveError(x.error));
    }

    isNew() {
        return this.formato.id === undefined;
    }

    private onSaveSuccess() {
        this.isSaving = false;
        this.messageService.add({
            severity: "success",
            summary: "Ok!",
            detail: this.isNew() ? "Formato creado":"Formato editado"
          });
        this.previousState();
    }

    private onSaveError(error:any) {
        this.messageService.add({
            severity: "error",
            summary: "ERROR",
            detail: this.isNew() ? "Hubo un error al crear el Formato\n" +" "+ error.message :"Hubo un error al editar el Formato" +" "+ error.message
          });
        this.isSaving = false;
    }

    get formato() {
        return this._formato;
    }

    set formato(formato: IFormato) {
        this._formato = formato;
    }
}
