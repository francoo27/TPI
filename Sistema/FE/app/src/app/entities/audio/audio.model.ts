export interface IAudio {
    id?: number;
    nombre?: string;
}

export class Audio implements IAudio {
    constructor(
        public id?: number,
        public nombre?: string,
    ) {

    }
}