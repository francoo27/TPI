
export interface ICompra {
    funcionId?:number;
    asientoIdSelected?:number[];
    precioIdQuantitySelected?:IPrecioSelectedQuantity[];
}

export class Compra implements ICompra {
    constructor(
        public funcionId?: number,
        public asientoIdSelected?: number[],
        public precioIdQuantitySelected?: IPrecioSelectedQuantity[],
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
