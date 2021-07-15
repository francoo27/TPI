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

    // create(formato: IGenero): Observable<EntityResponseType> {
    //     return this.http.post<IGenero>(this.resourceUrl, formato, { observe: 'response' });
    // }

    // update(formato: IGenero): Observable<EntityResponseType> {
    //     return this.http.put<IGenero>(`${this.resourceUrl}/${formato.id}`, formato, { observe: 'response' });
    // }

    // find(id: number): Observable<EntityResponseType> {
    //     return this.http.get<IGenero>(`${this.resourceUrl}/${id}`, { observe: 'response' });
    // }

    query(req?: any): Observable<EntityArrayResponseType> {
        // const options = createRequestOption(req);
        return this.http.get<IGenero[]>(this.resourceUrl, { params: {}/*options*/, observe: 'response' });
    }
}
