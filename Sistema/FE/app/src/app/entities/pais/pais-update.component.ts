import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { PaisService } from './pais.service';
import { IPais } from './pais.model';


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
        private activatedRoute: ActivatedRoute
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
        console.log(this.pais)
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

        this.previousState();
    }

    private onSaveError() {
        this.isSaving = false;
    }

    get pais() {
        return this._pais;
    }

    set pais(motivo: IPais) {
        this._pais = motivo;
    }
}
