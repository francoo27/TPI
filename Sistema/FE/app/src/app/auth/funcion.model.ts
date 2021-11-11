export interface IUser {
    email?: string;
    password?:string;
    token?:string;
}

export class IUser implements IUser {
    constructor(
        public email?: string,
        public password?:string,
        public token?:string,
    ) {

    }
}