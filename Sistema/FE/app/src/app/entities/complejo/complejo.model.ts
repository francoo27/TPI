export interface IComplejo {
    id?: number;
    nombre?: string;
    gerente?: string;
}

export class Complejo implements IComplejo {
    constructor(
        public id?: number,
        public nombre?: string,
        public gerente?: string,
    ) {

    }
}