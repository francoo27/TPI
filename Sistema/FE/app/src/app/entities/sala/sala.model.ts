import { IAsiento } from "../asiento/asiento.model";
import { IComplejo } from "../complejo/complejo.model";
import { IFormato } from "../formato/formato.model";

export interface ISala {
    id?: number;
    numero?: number;
    complejo?: IComplejo;
    formatos?: IFormato[];
    asientos?: IAsiento[];
}

export class Sala implements ISala {
    constructor(
        public id?: number,
        public nombre?: string,
        public complejo?: IComplejo,
        public formatos?: IFormato[],
        public asientos?: IAsiento[],
    ) {

    }
}