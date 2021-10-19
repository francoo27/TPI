import { Component } from '@angular/core';
import { IFormato } from '../formato/formato.model';
import { IFuncion } from '../funcion/funcion.model';
import { FuncionService } from '../funcion/funcion.service';
import { IPelicula } from '../pelicula/pelicula.model';
import { PeliculaService } from '../pelicula/pelicula.service';
import { Location } from '@angular/common';
import { IAsiento } from '../asiento/asiento.model';
import { IPrecio } from '../precio/precio.model';
import { PrecioService } from '../precio/precio.service';
import { isNgTemplate } from '@angular/compiler';

@Component({
    selector: 'car-boleteria',
    templateUrl: './boleteria.component.html',
    providers: []
})
export class BoleteriaComponent {
    peliculas:IPelicula[]=[];
    funciones:IFuncion[]=[];
    precios:any[]=[];

    peliculaSeleccionado!:IPelicula;
    formatoSeleccionado!:IFormato;
    funcionSeleccionado!:IFuncion;
    preciosSeleccionados:any[]=[];
    ccRegex: RegExp = /[0-9]{12}$/;
    cc!: string;  

    asientosSeleccionables : IAsiento[][] = []; 

    a: IAsiento[] = [{fila:1},{fila:2},{fila:3}];
    nodisp = [1,6,8,7,4,2]
    selected = [11,15,16]
    multi: IAsiento[][] = []; 

    constructor(private peliculaService: PeliculaService,
                private funcionService: FuncionService,
                private precioService: PrecioService,
                private location: Location
                ) { 
        this.peliculaService.query().subscribe(res=>{
            this.peliculas = res.body!;
        })
        this.precioService.query().subscribe(res=>{
            this.precios = res.body!;
            this.preciosSeleccionados = this.precios.map(x=>{
                x['cantidad'] = 0;
                return x;
            })
        })
    }

    onFormatoSelected() {
        console.log("asds")
        this.funcionService.queryByPeliculaAndFormato(this.peliculaSeleccionado.id!,this.formatoSeleccionado.id!).subscribe(res=>{
            this.funciones = res.body!;
        })
    }

    onPrecioChange(precio:IPrecio,value:string){
        this.preciosSeleccionados.forEach(x=> {
            if(x.id === precio.id){
                x['cantidad'] = parseInt(value);
            }
        })
        console.log(this.preciosSeleccionados);
    }

    calculateSubtotal(item:any) {
        return item.valor *  this.preciosSeleccionados.find(x=>x.id === item.id)['cantidad'];
    }

    calculateTotalElegido() {
        let subtotales = this.preciosSeleccionados.map(x=>x['cantidad']);
        let total = 0;
        subtotales.forEach(x=> total += x);
        return total;
    }

    calculateTotal() {
        let subtotales = this.preciosSeleccionados.map(x=>x['cantidad']*x.valor);
        let total = 0;
        subtotales.forEach(x=> total += x);
        return total;
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
