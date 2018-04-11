import { Component, Input } from '@angular/core';
import { Observable } from 'rxjs';
import { BaseFormElement } from '../../../../core/components';

@Component({
  selector: 'form-dropdown',
  templateUrl: './form-dropdown.component.html',
  styleUrls: ['./form-dropdown.component.scss']
})
export class FormDropdownComponent extends BaseFormElement {
  defaultValue = null;

  @Input() defaultText: string;
  @Input() enableDefault: boolean;
  @Input() dropdowns: Observable<any>;
  @Input() dropdownValueKey: string;
  @Input() dropdownTextKey: string;
}
