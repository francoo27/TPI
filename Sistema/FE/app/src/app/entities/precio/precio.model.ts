import { ITipoPrecio } from "../tipoPrecio/tipoPrecio.model";

export interface IPrecio {
    id?: number;
    valor?: number;
    tipoPrecio?: ITipoPrecio;
    activo?: boolean;
}

export class IAsiento implements IPrecio {
    constructor(
        public id?: number,
        public nombre?: string,
        public fila?: number,
        public columna?: number,
        public adaptado?: boolean,
        public activo?: boolean
    ) {
    }
}
