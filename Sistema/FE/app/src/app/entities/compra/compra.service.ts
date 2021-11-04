import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { SERVER_API_URL } from 'src/app/app.constants';
import { ICompra } from './compra.model';

type EntityResponseType = HttpResponse<ICompra>;
type EntityArrayResponseType = HttpResponse<ICompra[]>;

@Injectable({ providedIn: 'root' })
export class CompraService {
    private resourceUrl = SERVER_API_URL + 'api/compra';

    constructor(private http: HttpClient) {}

    buy_tickets_to_funcion(compra: ICompra): Observable<EntityResponseType> {
        // const options = createRequestOption(req);
        console.log(compra)
        return this.http.post<ICompra>(`${this.resourceUrl}`,compra, { observe: 'response' });;
    }
}
