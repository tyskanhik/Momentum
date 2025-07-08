import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable, of, tap } from 'rxjs';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CardsService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  /**
   * ToDo поменять any на модели данных
   */
  getCards(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/cards`).pipe(
      tap(data => data),
      catchError(error => {
        console.error('Ошибка при полученя данных', error)
        return of([])
      } 
    ))
  }
}
