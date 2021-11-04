
export interface ICompra {
    funcionId?:number;
    asientoIdSelected?:number[];
    precioIdQuantitySelected?:IPrecioSelectedQuantity[];
    email?: string;
    nombre?: string;
}

export class Compra implements ICompra {
    constructor(
        public funcionId?: number,
        public asientoIdSelected?: number[],
        public precioIdQuantitySelected?: IPrecioSelectedQuantity[],
        public email?: string,
        public nombre?: string,
    ) {
    }
}

export interface IPrecioSelectedQuantity {
    precioId?:number;
    quantity?:number;
}

export class PrecioSelectedQuantity implements IPrecioSelectedQuantity {
    constructor(
        public precioId?:number,
        public quantity?:number
    ) {}
}
