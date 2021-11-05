import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IAudio } from './audio.model';
import { SERVER_API_URL } from 'src/app/app.constants';

type EntityResponseType = HttpResponse<IAudio>;
type EntityArrayResponseType = HttpResponse<IAudio[]>;

@Injectable({ providedIn: 'root' })
export class AudioService {
    private resourceUrl = SERVER_API_URL + 'api/audio';

    constructor(private http: HttpClient) {}

    query(): Observable<EntityArrayResponseType> {
        return this.http.get<IAudio[]>(this.resourceUrl, { params: {}/*options*/, observe: 'response' });
    }

    create(audio: IAudio): Observable<EntityResponseType> {
        return this.http.post<IAudio>(this.resourceUrl, audio, { observe: 'response' });
    }

    update(audio: IAudio): Observable<EntityResponseType> {
        return this.http.put<IAudio>(`${this.resourceUrl}/${audio.id}`, audio, { observe: 'response' });
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<IAudio>(`${this.resourceUrl}/${id}`, { observe: 'response' });
    }

    delete(id: number): Observable<EntityResponseType> {
        return this.http.delete<IAudio>(`${this.resourceUrl}/${id}`, { observe: 'response' });
    }

}
