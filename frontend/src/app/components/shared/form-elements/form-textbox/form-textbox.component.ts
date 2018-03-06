import { Component, Input, OnInit } from '@angular/core';
import { BaseFormElement } from '../../../../core/components';

@Component({
  selector: 'form-textbox',
  templateUrl: './form-textbox.component.html',
  styleUrls: ['./form-textbox.component.scss']
})
export class FormTextboxComponent extends BaseFormElement implements OnInit {
  @Input() type: string;
  @Input() rows: number;
  @Input() cols: number;

  ngOnInit() {
    super.ngOnInit()
    this.type = this.type || "text";  // Defaults to the text type
  }
}