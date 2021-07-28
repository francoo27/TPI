import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ISala } from './sala.model';
import { SERVER_API_URL } from 'src/app/app.constants';

type EntityResponseType = HttpResponse<ISala>;
type EntityArrayResponseType = HttpResponse<ISala[]>;

@Injectable({ providedIn: 'root' })
export class SalaService {
    private resourceUrl = SERVER_API_URL + 'api/sala';

    constructor(private http: HttpClient) {}

    query(): Observable<EntityArrayResponseType> {
        return this.http.get<ISala[]>(this.resourceUrl, { params: {}/*options*/, observe: 'response' });
    }

    query_ByComplejo(complejoId:number): Observable<EntityArrayResponseType> {
        return this.http.get<ISala[]>(`${this.resourceUrl}/complejo/${complejoId}`, { params: {}/*options*/, observe: 'response' });
    }
}
