import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms'
import { BensService } from '../../shared/services/bens.service';
import { Location } from '@angular/common';
import { Bem } from '../../shared/bem.model'

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateComponent implements OnInit {

  bensForm: FormGroup;

  constructor(private bensService: BensService, private location: Location) { }

  ngOnInit(): void {

    const date = new Date
    const today = String(date.getFullYear()) + '-' + String(date.getMonth()+1) + '-' + String(date.getDate())

    this.bensForm = new FormGroup({

      'marca': new FormControl('', [Validators.required]), 
      'quantidade': new FormControl('', [Validators.required]),
      'valor_unitario': new FormControl('', [Validators.required]), 
      'inicio_garantia': new FormControl('', [Validators.required]),
      'termino_garantia': new FormControl('', [Validators.required]),
      'observacoes': new FormControl(''),
      'estado': new FormControl('bom'), 
      'situacao': new FormControl('em uso'),
      'data_cadastro': new FormControl(today),
      'tombamento': new FormControl('')
      
    })
  }

  onSubmit(){
    const newBem = this.bensForm.value
    newBem.tombamento = newBem.termino_garantia.split('-')[0] + '123456'
    this.bensService.create(newBem).subscribe( _ => location.reload())
  }

}
