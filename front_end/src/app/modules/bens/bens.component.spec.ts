import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BensComponent } from './bens.component';

describe('BensComponent', () => {
  let component: BensComponent;
  let fixture: ComponentFixture<BensComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BensComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BensComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
