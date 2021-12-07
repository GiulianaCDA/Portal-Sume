import { TestBed } from '@angular/core/testing';

import { BensService } from './bens.service';

describe('BensService', () => {
  let service: BensService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BensService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
