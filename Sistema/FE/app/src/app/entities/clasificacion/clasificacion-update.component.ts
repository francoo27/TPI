import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ClasificacionService } from './clasificacion.service';
import { IClasificacion } from './clasificacion.model';
import { MessageService } from 'primeng/api';
import { Location } from '@angular/common';


@Component({
    selector: 'car-clasificacion-update',
    templateUrl: './clasificacion-update.component.html'
})
export class ClasificacionUpdateComponent implements OnInit {
    private _clasificacion!: IClasificacion;
    currentIdentificador!: string;
    currentEdadMinima!: string;
    isSaving!: boolean;

    constructor(
        private paisService: ClasificacionService,
        private activatedRoute: ActivatedRoute,
        private messageService: MessageService,
        private location: Location
    ) {}

    ngOnInit() {
        this.isSaving = false;

        this.activatedRoute.data.subscribe(({ clasificacion }) => {
            this.clasificacion = clasificacion;
            this.currentIdentificador = clasificacion.identificador;
            this.currentEdadMinima = clasificacion.edadMinima
        });
    }

    previousState() {
        this.location.back();
    }

    save() {
        this.isSaving = true;
        if (this.isNew()) {
            this.subscribeToSaveResponse(this.paisService.create(this.clasificacion));
        } else {
            this.subscribeToSaveResponse(this.paisService.update(this.clasificacion));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<IClasificacion>>) {
        result.subscribe(() => this.onSaveSuccess(), () => this.onSaveError());
    }

    isNew() {
        return this.clasificacion.id === undefined;
    }

    private onSaveSuccess() {
        this.isSaving = false;
        this.messageService.add({
            severity: "success",
            summary: "Ok!",
            detail: this.isNew() ? "Clasificacion creada":"Clasificacion editada"
          });
        this.previousState();
    }

    private onSaveError() {
        this.messageService.add({
            severity: "error",
            summary: "Ok!",
            detail: this.isNew() ? "Hubo un error al crear la Clasificacion":"Hubo un error al editar la Clasificacion"
          });
        this.isSaving = false;
    }

    get clasificacion() {
        return this._clasificacion;
    }

    set clasificacion(clasificacion: IClasificacion) {
        this._clasificacion = clasificacion;
    }
}
