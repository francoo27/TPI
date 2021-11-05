export interface ITecnologiaProyeccion {
    id?: number;
    nombre?: string;
}

export class TecnologiaProyeccion implements ITecnologiaProyeccion {
    constructor(
        public id?: number,
        public nombre?: string,
    ) {

    }
}