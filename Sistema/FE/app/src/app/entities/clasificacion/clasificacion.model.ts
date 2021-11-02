export interface IClasificacion {
    id?: number;
    nombre?: string;
    identificador?: string;
    edadMinima?: number;
    recomendacion?: string;
    definicion?: string;
}

export class Clasificacion implements IClasificacion {
    constructor(
        public id?: number,
        public nombre?: string,
        public identificador?: string,
        public edadMinima?: number,
        public recomendacion?: string,
        public definicion?: string,
    ) {}
}