import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IGenero } from './genero.model';
import { SERVER_API_URL } from 'src/app/app.constants';

type EntityResponseType = HttpResponse<IGenero>;
type EntityArrayResponseType = HttpResponse<IGenero[]>;

@Injectable({ providedIn: 'root' })
export class GeneroService {
    private resourceUrl = SERVER_API_URL + 'api/genero';

    constructor(private http: HttpClient) {}

    query(): Observable<EntityArrayResponseType> {
        return this.http.get<IGenero[]>(this.resourceUrl, { params: {}/*options*/, observe: 'response' });
    }
}
