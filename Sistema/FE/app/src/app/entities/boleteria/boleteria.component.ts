import { Component, OnInit } from '@angular/core';
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
import { ActivatedRoute } from '@angular/router';
import { AsientoService } from '../asiento/asiento.service';
import { CompraService } from '../compra/compra.service';
import { Compra, PrecioSelectedQuantity } from '../compra/compra.model';

@Component({
    selector: 'car-boleteria',
    templateUrl: './boleteria.component.html',
    providers: []
})
export class BoleteriaComponent implements OnInit {
    peliculas:IPelicula[]=[];
    funciones:IFuncion[]=[];
    precios:any[]=[];

    peliculaSeleccionado!:IPelicula;
    formatoSeleccionado!:IFormato;
    funcionSeleccionado!:IFuncion;
    preciosSeleccionados:any[]=[];
    ccRegex: RegExp = /[0-9]{12}$/;
    cc!: string;
    me!: string;  
    ae!: string;  
    cvef!: string;
    
    okPrecio:boolean = false;
    okAsiento:boolean = false;

    asientosSeleccionables : IAsiento[][] = []; 

    a: IAsiento[] = [{fila:1},{fila:2},{fila:3}];
    nodisp:number[] = []
    selected:number[] = []
    multi: IAsiento[][] = []; 

    constructor(private peliculaService: PeliculaService,
                private funcionService: FuncionService,
                private precioService: PrecioService,
                private location: Location,
                private activatedRoute: ActivatedRoute,
                private asientoService: AsientoService,
                private compraService: CompraService
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


    ngOnInit() {
        this.activatedRoute.data.subscribe(({ pelicula }) => {
            this.peliculaSeleccionado = pelicula;
        });
    }

    onFormatoSelected() {
        this.funcionService.queryByPeliculaAndFormato(this.peliculaSeleccionado.id!,this.formatoSeleccionado.id!).subscribe(res=>{
            this.funciones = res.body!;
        })
    }

    onPrecioChange(precio:IPrecio,value:string){
        this.preciosSeleccionados.forEach(x=> {
            if(x.id === precio.id){
                let val = parseInt(value)
                x['cantidad'] = !isNaN(val) ? val : 0;
            }
        })
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

    isPrecioSelected(){
        return this.preciosSeleccionados.some(x=>x['cantidad']>0);
    }
    
    calculateTotalPrecioSelected(){
        return this.preciosSeleccionados.reduce((a, b) => a + b['cantidad'], 0);
    }

    calculateTotal() {
        let subtotales = this.preciosSeleccionados.map(x=>x['cantidad']*x.valor);
        let total = 0;
        subtotales.forEach(x=> total += x);
        return total;
    }

    onFuncionSelected() {
        this.asientoService.query_occupied_by_funcion(this.funcionSeleccionado.id!).subscribe(res=>{
            this.nodisp = res.body!.map(x => x.id!);
            this.fillAsientos()
        })
    }

    previousState() {
        this.location.back();
    }

    isDisabled(): boolean {
        return false;
    }

    onAsientoSelected(id:number){
        if (this.selected.length >= this.calculateTotalPrecioSelected() && !this.selected.some(x =>x == id)) {
            return;
        }
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
        this.asientosSeleccionables = []
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
            // console.log(this.asientosSeleccionables);
            ini++;
        }
    }

    canPagar(){
        return this.selected.length > 0 && this.selected.length == this.calculateTotalPrecioSelected();
    }


    onSubmit(){
        console.log(this.funcionSeleccionado);
        console.log(this.selected)
        console.log(this.preciosSeleccionados.map(x=>{return new PrecioSelectedQuantity(x.id,x['cantidad'])}))
        this.compraService.buy_tickets_to_funcion(new Compra(this.funcionSeleccionado.id!,this.selected,this.preciosSeleccionados.map(x=>{return new PrecioSelectedQuantity(x.id,x['cantidad'])}))).subscribe()
    }

}
