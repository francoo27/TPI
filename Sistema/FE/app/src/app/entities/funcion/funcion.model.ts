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