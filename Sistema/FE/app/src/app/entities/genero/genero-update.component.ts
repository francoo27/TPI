import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { GeneroService } from './genero.service';
import { IGenero } from './genero.model';
import { MessageService } from 'primeng/api';
import { Location } from '@angular/common';


@Component({
    selector: 'car-genero-update',
    templateUrl: './genero-update.component.html'
})
export class GeneroUpdateComponent implements OnInit {
    private _genero!: IGenero;
    currentNombre!: string;
    isSaving!: boolean;

    constructor(
        private paisService: GeneroService,
        private activatedRoute: ActivatedRoute,
        private messageService: MessageService,
        private location: Location
    ) {}

    ngOnInit() {
        this.isSaving = false;

        this.activatedRoute.data.subscribe(({ genero }) => {
            this.genero = genero;
            this.currentNombre = genero.nombre;
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
            this.subscribeToSaveResponse(this.paisService.create(this.genero));
        } else {
            this.subscribeToSaveResponse(this.paisService.update(this.genero));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<IGenero>>) {
        result.subscribe(() => this.onSaveSuccess(), () => this.onSaveError());
    }

    isNew() {
        return this.genero.id === undefined;
    }

    private onSaveSuccess() {
        this.isSaving = false;
        this.messageService.add({
            severity: "success",
            summary: "Ok!",
            detail: this.isNew() ? "Genero creado":"Genero editado"
          });
        this.previousState();
    }

    private onSaveError() {
        this.messageService.add({
            severity: "error",
            summary: "Ok!",
            detail: this.isNew() ? "Hubo un error al crear el Genero":"Hubo un error al editar el Genero"
          });
        this.isSaving = false;
    }

    get genero() {
        return this._genero;
    }

    set genero(genero: IGenero) {
        this._genero = genero;
    }
}
