import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AudioService } from './audio.service';
import { IAudio } from './audio.model';
import { MessageService } from 'primeng/api';
import { Location } from '@angular/common';


@Component({
    selector: 'car-audio-update',
    templateUrl: './audio-update.component.html'
})
export class AudioUpdateComponent implements OnInit {
    private _audio!: IAudio;
    currentNombre!: string;
    isSaving!: boolean;

    constructor(
        private audioService: AudioService,
        private activatedRoute: ActivatedRoute,
        private messageService: MessageService,
        private location: Location
    ) {}

    ngOnInit() {
        this.isSaving = false;

        this.activatedRoute.data.subscribe(({ audio }) => {
            this.audio = audio;
            this.currentNombre = audio.nombre;
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
            this.subscribeToSaveResponse(this.audioService.create(this.audio));
        } else {
            this.subscribeToSaveResponse(this.audioService.update(this.audio));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<IAudio>>) {
        result.subscribe(() => this.onSaveSuccess(), () => this.onSaveError());
    }

    isNew() {
        return this.audio.id === undefined;
    }

    private onSaveSuccess() {
        this.isSaving = false;
        this.messageService.add({
            severity: "success",
            summary: "Ok!",
            detail: this.isNew() ? "Audio creado":"Audio editado"
          });
        this.previousState();
    }

    private onSaveError() {
        this.messageService.add({
            severity: "error",
            summary: "Ok!",
            detail: this.isNew() ? "Hubo un error al crear el Audio":"Hubo un error al editar el Audio"
          });
        this.isSaving = false;
    }

    get audio() {
        return this._audio;
    }

    set audio(audio: IAudio) {
        this._audio = audio;
    }
}
