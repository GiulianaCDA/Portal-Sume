import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from "@angular/common/http"
import { Observable } from 'rxjs';
import { Bem } from '../bem.model'

@Injectable({
  providedIn: 'root'
})
export class BensService {

  constructor(public http: HttpClient) { }
  private httpOptions = {headers: new HttpHeaders({ 'Content-Type': 'application/json' })};
  private bensUrl = 'http://localhost:3000/bens'

  getAll(): Observable<Bem[]>{

    return this.http.get<Bem[]>(this.bensUrl)
    
  }

  create(bem: Bem): Observable<Bem>{

    return this.http.post<Bem>(this.bensUrl, bem, this.httpOptions)
  }

  delete(bem: Bem | number): Observable<Bem>{
    const id = typeof bem == 'number' ? bem : bem.id
    const url = `${this.bensUrl}/${id}`;
    console.log(url)
    return this.http.delete<Bem>(url, this.httpOptions)
  }
}
