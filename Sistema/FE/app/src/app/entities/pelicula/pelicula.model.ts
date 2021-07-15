import { IClasificacion } from "../clasifiacion/clasificacion.model";
import { IFormato } from "../formato/formato.model";
import { IPais } from "../pais/pais.model";

export interface IPelicula {
    id?: number;
    nombre?: string;
    codigo?: string;
    tituloOriginal?: string;
    tituloPais?: string;
    fechaEstreno?: string;
    imagen?: string;
    duracion?: number;
    sinopsis?: string;
    clasificacion?: IClasificacion;
    pais?: IPais;
    //genero?: IGenero;
    formatos?: IFormato[];
}

export class Pelicula implements IPelicula {
    constructor(
        public id?: number,
        public nombre?: string,
        public codigo?: string,
        public tituloOriginal?: string,
        public tituloPais?: string,
        public fechaEstreno?: string,
        public duracion?: number,
        public sinopsis?: string,
        clasificacion?: IClasificacion,
        public pais?: IPais,
        //genero?: IGenero;
        public formatos?: IFormato[]
    ) {

    }
}