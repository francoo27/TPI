import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { PaisService } from './pais.service';
import { IPais } from './pais.model';
import { MessageService } from 'primeng/api';


@Component({
    selector: 'car-pais-update',
    templateUrl: './pais-update.component.html'
})
export class PaisUpdateComponent implements OnInit {
    private _pais!: IPais;
    currentNombre!: string;
    isSaving!: boolean;

    constructor(
        private paisService: PaisService,
        private activatedRoute: ActivatedRoute,
        private messageService: MessageService
    ) {}

    ngOnInit() {
        this.isSaving = false;

        this.activatedRoute.data.subscribe(({ pais }) => {
            this.pais = pais;
            this.currentNombre = pais.nombre;
        });
    }

    previousState() {
        window.history.back();
    }

    onSubmit(){
        console.log("asds")
    }

    save() {
        this.isSaving = true;
        if (this.isNew()) {
            this.subscribeToSaveResponse(this.paisService.create(this.pais));
        } else {
            this.subscribeToSaveResponse(this.paisService.update(this.pais));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<IPais>>) {
        result.subscribe(() => this.onSaveSuccess(), () => this.onSaveError());
    }

    isNew() {
        return this.pais.id === undefined;
    }

    private onSaveSuccess() {
        this.isSaving = false;
        this.messageService.add({
            severity: "success",
            summary: "Ok!",
            detail: this.isNew() ? "Pais creado":"Pais editado"
          });
        this.previousState();
    }

    private onSaveError() {
        this.messageService.add({
            severity: "error",
            summary: "Ok!",
            detail: this.isNew() ? "Hubo un error al crear el Pais":"Hubo un error al editar el Pais"
          });
        this.isSaving = false;
    }

    get pais() {
        return this._pais;
    }

    set pais(motivo: IPais) {
        this._pais = motivo;
    }
}
