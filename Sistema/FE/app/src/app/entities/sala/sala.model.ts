export interface ISala {
    id?: number;
    nombre?: string;
    codigo?: string;
}

export class Sala implements ISala {
    constructor(
        public id?: number,
        public nombre?: string,
    ) {

    }
}