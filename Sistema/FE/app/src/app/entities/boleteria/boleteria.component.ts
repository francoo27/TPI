import { Component } from '@angular/core';
import { IFormato } from '../formato/formato.model';
import { IFuncion } from '../funcion/funcion.model';
import { FuncionService } from '../funcion/funcion.service';
import { IPelicula } from '../pelicula/pelicula.model';
import { PeliculaService } from '../pelicula/pelicula.service';

@Component({
    selector: 'car-boleteria',
    templateUrl: './boleteria.component.html',
    providers: []
})
export class BoleteriaComponent {
    peliculas:IPelicula[]=[];
    funciones:IFuncion[]=[];
    peliculaSeleccionado!:IPelicula;
    formatoSeleccionado!:IFormato;
    funcionSeleccionado!:IFuncion;
    ccRegex: RegExp = /[0-9]{12}$/;
    cc!: string;  

    constructor(private peliculaService: PeliculaService,
                private funcionService: FuncionService
                ) { 
        this.peliculaService.query().subscribe(res=>{
            this.peliculas = res.body!;
        })
    }

    onFormatoSelected() {
        console.log("asds")
        this.funcionService.queryByPeliculaAndFormato(this.peliculaSeleccionado.id!,this.formatoSeleccionado.id!).subscribe(res=>{
            this.funciones = res.body!;
        })
    }

    ngOnInit() {}

}
