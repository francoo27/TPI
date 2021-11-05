import { Component, OnInit, OnDestroy } from '@angular/core';
import {MessageService} from 'primeng/api';
import { IAudio } from './audio.model';
import { AudioService } from './audio.service';

@Component({
    selector: 'car-audio',
    templateUrl: './audio.component.html',
    providers: []
})
export class AudioComponent implements OnInit, OnDestroy {
    audios: IAudio[] =  [];

    constructor(
        private audioService: AudioService,
        private messageService: MessageService
    ) {
    }

    ngOnInit(): void {
      this.audioService.query().subscribe(res => {
        this.audios = res.body!
    } );

    }

    delete(id:number):void{
        this.audioService.delete(id).subscribe(
            x => {
                setTimeout(() => {
                    this.messageService.add({
                        severity: "success",
                        summary: "Todo Ok!",
                        detail:"Audio Eliminado"
                    })
                }, 100);
            },
            res => {
                setTimeout(() => {
                    this.messageService.add({
                        severity: "error",
                        summary: "ERROR",
                        detail:res.error.message
                    })
                }, 100);
            },
            () => {
                this.audioService.query().subscribe(res => {
                    this.audios = res.body!
                });
            }
        );
    }

    ngOnDestroy(): void {}
}
