import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { SERVER_API_URL } from 'src/app/app.constants';
import { IUser } from './funcion.model';

type EntityResponseType = HttpResponse<IUser>;
type EntityResponseCreateType = HttpResponse<IUser>;

@Injectable({ providedIn: 'root' })
export class AuthService {
    private resourceUrl = SERVER_API_URL + 'api/authorization';

    constructor(private http: HttpClient) {}

    login(user: IUser): Observable<EntityResponseType> {
        return this.http.post<IUser>(`${this.resourceUrl}/login`, user, { observe: 'response' });
    }

    logout(user: IUser): Observable<EntityResponseType> {
        return this.http.post<IUser>(`${this.resourceUrl}/logout`, user, { observe: 'response' });
    }
    
    authenticate(user: IUser): Observable<EntityResponseType> {
        return this.http.get<IUser>(`${this.resourceUrl}/${user.token}`, { observe: 'response' });
    }
}
