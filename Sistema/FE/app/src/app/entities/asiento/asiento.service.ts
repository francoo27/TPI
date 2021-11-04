import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IAsiento } from './asiento.model';
import { SERVER_API_URL } from 'src/app/app.constants';

type EntityResponseType = HttpResponse<IAsiento>;
type EntityArrayResponseType = HttpResponse<IAsiento[]>;

@Injectable({ providedIn: 'root' })
export class AsientoService {
    private resourceUrl = SERVER_API_URL + 'api/asiento';

    constructor(private http: HttpClient) {}

    query_occupied_by_funcion(funcion_id: number): Observable<EntityArrayResponseType> {
        // const options = createRequestOption(req);
        return this.http.get<IAsiento[]>(`${this.resourceUrl}/funcion/${funcion_id}`, { params: {}/*options*/, observe: 'response' });
    }
}
