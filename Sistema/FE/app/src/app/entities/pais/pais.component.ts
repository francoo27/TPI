import { Component, OnInit, OnDestroy } from '@angular/core';
import {MessageService} from 'primeng/api';
import { PaisService } from './pais.service';

@Component({
    selector: 'car-pais',
    templateUrl: './pais.component.html',
    providers: []
})
export class PaisComponent implements OnInit, OnDestroy {
    countries: any[] =  [{
        name: 'Australia',
        code: 'AU'
    }];
    selectedCity1: any;


    constructor(
        private paisService: PaisService,
        private messageService: MessageService
    ) {
    }

    ngOnInit(): void {
      this.paisService.query().subscribe(res => {
        this.countries = res.body!
    } );

    }

    ngOnDestroy(): void {}
}
