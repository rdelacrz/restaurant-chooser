import { Component, Input, ContentChildren, QueryList } from '@angular/core';
import { BaseFormElement } from '../../../../core/components';
import { FormTextboxComponent } from "../form-textbox/form-textbox.component";

@Component({
  selector: 'form-row',
  templateUrl: './form-row.component.html',
  styleUrls: ['./form-row.component.scss']
})
export class FormRowComponent extends BaseFormElement {
  @ContentChildren("formElement") formTextboxes : QueryList<BaseFormElement>;

  htmlContent : any;

  ngAfterViewChecked() {
  }
}