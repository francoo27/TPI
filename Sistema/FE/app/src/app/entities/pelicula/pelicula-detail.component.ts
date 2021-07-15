import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { IPelicula } from './pelicula.model';

@Component({
    selector: 'car-pelicula-detail',
    templateUrl: './pelicula-detail.component.html'
})
export class PeliculaDetailComponent implements OnInit {
    pelicula!: IPelicula;

    constructor(private activatedRoute: ActivatedRoute) {}

    ngOnInit(): void {
        this.activatedRoute.data.subscribe(({ pelicula }) => this.pelicula = pelicula);
    }
}
