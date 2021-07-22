export interface IFormato {
    id?: number;
    nombre?: string;
}

export class Formato implements IFormato {
    constructor(
        public id?: number,
        public nombre?: string,
    ) {

    }
}