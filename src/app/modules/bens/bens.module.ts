import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { BensRoutingModule } from './bens-routing.module';
import { IndexComponent } from './components/index/index.component';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';



@NgModule({
  declarations: [
    IndexComponent,
  ],
  imports: [
    CommonModule,
    BensRoutingModule,
    FormsModule,
    ReactiveFormsModule
  ]
})
export class BensModule { }
