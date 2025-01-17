import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IClasificacion } from './clasificacion.model';
import { SERVER_API_URL } from 'src/app/app.constants';

type EntityResponseType = HttpResponse<IClasificacion>;
type EntityArrayResponseType = HttpResponse<IClasificacion[]>;

@Injectable({ providedIn: 'root' })
export class ClasificacionService {
    private resourceUrl = SERVER_API_URL + 'api/clasificacion';

    constructor(private http: HttpClient) {}
    
    query(): Observable<EntityArrayResponseType> {
        return this.http.get<IClasificacion[]>(this.resourceUrl, { params: {}/*options*/, observe: 'response' });
    }

    create(clasificacion: IClasificacion): Observable<EntityResponseType> {
        return this.http.post<IClasificacion>(this.resourceUrl, clasificacion, { observe: 'response' });
    }

    update(clasificacion: IClasificacion): Observable<EntityResponseType> {
        return this.http.put<IClasificacion>(`${this.resourceUrl}/${clasificacion.id}`, clasificacion, { observe: 'response' });
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<IClasificacion>(`${this.resourceUrl}/${id}`, { observe: 'response' });
    }

    delete(id: number): Observable<EntityResponseType> {
        return this.http.delete<IClasificacion>(`${this.resourceUrl}/${id}`, { observe: 'response' });
    }
}
