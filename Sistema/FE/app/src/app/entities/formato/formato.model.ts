import { IAudio } from "../audio/audio.model";
import { ITecnologiaProyeccion } from "../tecnologia-proyeccion/tecnologia-proyeccion.model";

export interface IFormato {
    id?: number;
    nombre?: string;
    tecnologiaProyeccion?:ITecnologiaProyeccion;
    audio?:IAudio;
}

export class Formato implements IFormato {
    constructor(
        public id?: number,
        public nombre?: string,
        public tecnologiaProyeccion?:ITecnologiaProyeccion,
        public audio?:IAudio
    ) {

    }
}