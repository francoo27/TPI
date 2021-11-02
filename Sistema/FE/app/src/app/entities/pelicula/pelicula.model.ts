import { IClasificacion } from "../clasificacion/clasificacion.model";
import { IFormato } from "../formato/formato.model";
import { IGenero } from "../genero/genero.model";
import { IPais } from "../pais/pais.model";

export interface IPelicula {
    id?: number;
    tituloOriginal?: string;
    tituloPais?: string;
    fechaEstreno?: string;
    imagen?: string | null;
    duracion?: number;
    sinopsis?: string;
    clasificacion?: IClasificacion;
    pais?: IPais;
    genero?: IGenero;
    formatos?: IFormato[];
}

export class Pelicula implements IPelicula {
    constructor(
        public id?: number,
        public tituloOriginal?: string,
        public tituloPais?: string,
        public fechaEstreno?: string,
        public duracion?: number,
        public sinopsis?: string,
        public imagen?: string | null,
        public clasificacion?: IClasificacion,
        public pais?: IPais,
        public genero?: IGenero,
        public formatos?: IFormato[]
    ) {

    }
}