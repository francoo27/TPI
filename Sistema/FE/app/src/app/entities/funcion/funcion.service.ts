import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IFuncion } from './funcion.model';
import { SERVER_API_URL } from 'src/app/app.constants';

type EntityResponseType = HttpResponse<IFuncion>;
type EntityArrayResponseType = HttpResponse<IFuncion[]>;

@Injectable({ providedIn: 'root' })
export class FuncionService {
    private resourceUrl = SERVER_API_URL + 'api/funcion';

    constructor(private http: HttpClient) {}

    create(funcion: IFuncion): Observable<EntityResponseType> {
        return this.http.post<IFuncion>(this.resourceUrl, funcion, { observe: 'response' });
    }

    update(funcion: IFuncion): Observable<EntityResponseType> {
        return this.http.put<IFuncion>(`${this.resourceUrl}/${funcion.id}`, funcion, { observe: 'response' });
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<IFuncion>(`${this.resourceUrl}/${id}`, { observe: 'response' });
    }

    query(req?: any): Observable<EntityArrayResponseType> {
        // const options = createRequestOption(req);
        return this.http.get<IFuncion[]>(this.resourceUrl, { params: {}/*options*/, observe: 'response' });
    }
        
    queryByPeliculaAndFormato(peliculaId:number,formatoId:number): Observable<EntityArrayResponseType> {
        // const options = createRequestOption(req);
        return this.http.get<IFuncion[]>(`${this.resourceUrl}/pelicula/${peliculaId}/formato/${formatoId}`, { params: {}/*options*/, observe: 'response' });
    }
}
