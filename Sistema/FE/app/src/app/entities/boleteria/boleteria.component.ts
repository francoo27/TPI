import { Component } from '@angular/core';
import { IFormato } from '../formato/formato.model';
import { IFuncion } from '../funcion/funcion.model';
import { FuncionService } from '../funcion/funcion.service';
import { IPelicula } from '../pelicula/pelicula.model';
import { PeliculaService } from '../pelicula/pelicula.service';
import { Location } from '@angular/common';
import { IAsiento } from '../asiento/asiento.model';

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

    asientosSeleccionables : IAsiento[][] = []; 

    a: IAsiento[] = [{fila:1},{fila:2},{fila:3}];
    nodisp = [1,6,8,7,4,2]
    selected = [11,15,16]
    multi: IAsiento[][] = []; 

    constructor(private peliculaService: PeliculaService,
                private funcionService: FuncionService,
                private location: Location
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

    onFuncionSelected() {
        this.fillAsientos()
    }

    ngOnInit() {}

    previousState() {
        this.location.back();
    }

    isDisabled(): boolean {
        return false;
    }

    onAsientoSelected(id:number){
        this.asientosSeleccionables.map(x => {
            return x.map(y=>{
                if(y.id === id){
                    y.seleccionado = !y.seleccionado;
                    if(y.seleccionado){
                        this.selected.push(id);
                    }else{
                        this.selected = [...this.selected.filter(z => z !== id)];
                    }
                }
            })
        } );
        console.log(this.selected)
    }

    fillAsientos(){
        let ini = 1;
        let arr : IAsiento[] = [];
        while (true) {
            arr = this.funcionSeleccionado.sala?.asientos!.filter(x => x.fila == ini)!;
            arr = arr.map(x => {
                let result = this.nodisp.find(y=> y == x.id);
                let result2 = this.selected.find(y => y == x.id);
                x.disponible = result === null  || result === undefined;
                x.seleccionado = result2 !== null  && result2 !== undefined;
                return x})
            if (arr.length < 1) {break;}
            this.asientosSeleccionables.push([...arr]);
            console.log(this.asientosSeleccionables);
            ini++;
        }
    }

}
