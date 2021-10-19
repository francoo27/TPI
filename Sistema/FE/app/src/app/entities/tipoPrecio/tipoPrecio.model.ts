export interface ITipoPrecio {
    id?: number;
    nombre?: string;
    codigo?: string;
}

export class IAsiento implements ITipoPrecio {
    constructor(
        public id?: number,
        public codigo?: string,
        public nombre?: string,
    ) {
    }
}