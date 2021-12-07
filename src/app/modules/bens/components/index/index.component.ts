import { Component, OnInit } from '@angular/core';
import {Bem} from '../../shared/bem.model'
import { BensService } from '../../shared/services/bens.service';
import { Location } from '@angular/common';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.scss']
})
export class IndexComponent implements OnInit {

  bens: Bem[];

  constructor(private bensService: BensService ) { }

  ngOnInit(): void {
    this.bensService.getAll()
    .subscribe(f => this.bens = f)
  }

  del(bem: Bem){
    this.bensService.delete(bem) 
    .subscribe( _ => location.reload())
  }


}
