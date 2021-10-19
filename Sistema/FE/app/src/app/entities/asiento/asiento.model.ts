export interface IAsiento {
    id?: number;
    nombre?: string;
    fila?: number;
    columna?: number;
    adaptado?: boolean;
}

export class IAsiento implements IAsiento {
    constructor(
        public id?: number,
        public nombre?: string,
        public fila?: number,
        public columna?: number,
        public adaptado?: boolean,
        public disponible?: boolean,
        public seleccionado?: boolean
    ) {
    }
}