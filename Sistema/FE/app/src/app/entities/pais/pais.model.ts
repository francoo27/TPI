export interface IPais {
    id?: number;
    nombre?: string;
    codigo?: string;
}

export class Pais implements IPais {
    constructor(
        public id?: number,
        public nombre?: string,
        public codigo?: string
    ) {

    }
}