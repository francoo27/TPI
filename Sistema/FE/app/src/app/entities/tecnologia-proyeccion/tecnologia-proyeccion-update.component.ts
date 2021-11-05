import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { TecnologiaProyeccionService } from './tecnologia-proyeccion.service';
import { ITecnologiaProyeccion } from './tecnologia-proyeccion.model';
import { MessageService } from 'primeng/api';
import { Location } from '@angular/common';


@Component({
    selector: 'car-tecnologia-proyeccion-update',
    templateUrl: './tecnologia-proyeccion-update.component.html'
})
export class TecnologiaProyeccionUpdateComponent implements OnInit {
    private _tecnologiaProyeccion!: ITecnologiaProyeccion;
    currentNombre!: string;
    isSaving!: boolean;

    constructor(
        private tecnologiaProyeccionService: TecnologiaProyeccionService,
        private activatedRoute: ActivatedRoute,
        private messageService: MessageService,
        private location: Location
    ) {}

    ngOnInit() {
        this.isSaving = false;

        this.activatedRoute.data.subscribe(({ tecnologiaProyeccion }) => {
            this.tecnologiaProyeccion = tecnologiaProyeccion;
            this.currentNombre = tecnologiaProyeccion.nombre;
        });
    }

    previousState() {
        this.location.back();
    }

    onSubmit(){
        console.log("asds")
    }

    save() {
        this.isSaving = true;
        if (this.isNew()) {
            this.subscribeToSaveResponse(this.tecnologiaProyeccionService.create(this.tecnologiaProyeccion));
        } else {
            this.subscribeToSaveResponse(this.tecnologiaProyeccionService.update(this.tecnologiaProyeccion));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<ITecnologiaProyeccion>>) {
        result.subscribe(() => this.onSaveSuccess(), () => this.onSaveError());
    }

    isNew() {
        return this.tecnologiaProyeccion.id === undefined;
    }

    private onSaveSuccess() {
        this.isSaving = false;
        this.messageService.add({
            severity: "success",
            summary: "Ok!",
            detail: this.isNew() ? "Tecnologia de Proyeccion creada":"Tecnologia de Proyeccion editada"
          });
        this.previousState();
    }

    private onSaveError() {
        this.messageService.add({
            severity: "error",
            summary: "Ok!",
            detail: this.isNew() ? "Hubo un error al crear la Tecnologia de Proyeccion":"Hubo un error al editar la Tecnologia de Proyeccion"
          });
        this.isSaving = false;
    }

    get tecnologiaProyeccion() {
        return this._tecnologiaProyeccion;
    }

    set tecnologiaProyeccion(tecnologiaProyeccion: ITecnologiaProyeccion) {
        this._tecnologiaProyeccion = tecnologiaProyeccion;
    }
}
