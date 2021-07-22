export interface IGenero {
    id?: number;
    nombre?: string;
}

export class Genero implements IGenero {
    constructor(
        public id?: number,
        public nombre?: string,
    ) {

    }
}