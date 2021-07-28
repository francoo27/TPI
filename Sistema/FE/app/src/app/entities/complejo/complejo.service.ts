import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IComplejo } from './complejo.model';
import { SERVER_API_URL } from 'src/app/app.constants';

type EntityResponseType = HttpResponse<IComplejo>;
type EntityArrayResponseType = HttpResponse<IComplejo[]>;

@Injectable({ providedIn: 'root' })
export class ComplejoService {
    private resourceUrl = SERVER_API_URL + 'api/complejo';

    constructor(private http: HttpClient) {}

    query(): Observable<EntityArrayResponseType> {
        return this.http.get<IComplejo[]>(this.resourceUrl, { params: {}/*options*/, observe: 'response' });
    }
}
