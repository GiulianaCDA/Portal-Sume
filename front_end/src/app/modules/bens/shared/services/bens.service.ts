import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from "@angular/common/http"
import { Observable } from 'rxjs';
import { Bem } from '../bem.model'
import { Fornecedor } from '../fornecedor.model'
import { Nota } from '../nota.model'

@Injectable({
  providedIn: 'root'
})
export class BensService {

  constructor(public http: HttpClient) { }
  private httpOptions = {headers: new HttpHeaders({ 'Content-Type': 'application/json' })};
  private bensUrl = 'http://localhost:8000/bens/'
  private fornecedoresUrl = 'http://localhost:8000/fornecedores/'
  private notasUrl = 'http://localhost:8000/notasfiscais/'

  getAll(): Observable<Bem[]>{

    return this.http.get<Bem[]>(this.bensUrl)
    
  }

  getFornecedores(): Observable<Fornecedor[]>{

    return this.http.get<Fornecedor[]>(this.fornecedoresUrl)
    
  }

  getNota(): Observable<Nota[]>{

    return this.http.get<Nota[]>(this.notasUrl)
    
  }

  create(bem: Bem): Observable<Bem>{
    /* Cria no db.json */
    return this.http.post<Bem>('http://localhost:3000/bens', bem, this.httpOptions)
  }

  delete(bem: Bem | number): Observable<Bem>{
    const id = typeof bem == 'number' ? bem : bem.id_bem
    const url = `${this.bensUrl}${id}/`;
    console.log(url)
    return this.http.delete<Bem>(url, this.httpOptions)
  }
}
