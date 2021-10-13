import { IFormato } from "../formato/formato.model";
import { IPelicula } from "../pelicula/pelicula.model";
import { ISala } from "../sala/sala.model";

export interface IFuncion {
    id?: number;
    nombre?: string;
    fechaInicio?:string;
    horaInicio?:string;
    pelicula?: IPelicula;
    formato?: IFormato;
    sala?: ISala;

}

export class Funcion implements IFuncion {
    constructor(
        public id?: number,
        public nombre?: string,
        public fechaInicio?:string,
        public horaInicio?:string,
        public pelicula?: IPelicula,
        public formato?: IFormato,
        public sala?: ISala,
    ) {

    }
}

export interface IFuncionCreate {
    id?: number;
    nombre?: string;
    fechaInicio?:string;
    fechaDia?:number;
    fechaMes?:number;
    fechaAnio?:number;
    horaInicio?:string;
    peliculaId?: number;
    formatoId?: number;
    salaId?: number;
    hora?: number;
    minuto?: number;
}

export class FuncionCreate implements IFuncionCreate {
    constructor(
        public id?: number,
        public nombre?: string,
        public fechaInicio?:string,
        public horaInicio?:string,
        public peliculaId?: number,
        public formatoId?: number,
        public salaId?: number,
        public fechaDia?:number,
        public fechaMes?:number,
        public fechaAnio?:number,
        public hora?:number,
        public minuto?:number,
    ) {

    }
}

export function mapToFuncionCreate(funcion:IFuncion): IFuncionCreate{
    return new FuncionCreate(funcion.id,funcion.nombre,funcion.fechaInicio,funcion.horaInicio,funcion.pelicula?.id,funcion.formato?.id,funcion.sala?.id);
}