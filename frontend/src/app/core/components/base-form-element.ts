import { EventEmitter, Input, OnInit, Output, ViewChild } from '@angular/core';
import { NgForm, NgModel } from '@angular/forms';

export class BaseFormElement implements OnInit {
  @ViewChild("formElement") formElement: NgModel;

  @Input() parentForm: NgForm;
  @Input() elementName: string;
  @Input() label: string;
  @Input() labelColNum: number;
  @Input() fieldColNum: number;
  @Input() isReadOnly: boolean;
  @Input() isDisabled: boolean;
  @Input() isRequired: boolean;
  @Input() placeholder: string;
  @Input() min: number;
  @Input() max: number;
  @Input() maxLength: number;
  @Input() model: any;

  @Output() modelChange = new EventEmitter<any>();

  // Field classes
  labelClass = "";
  fieldClass = "";

  ngOnInit() {
    // Adds col-sm classes
    if (this.labelColNum)
      this.labelClass = "col-sm-" + this.labelColNum;
    if (this.fieldColNum)
      this.fieldClass = "col-sm-" + this.fieldColNum;

    // Adds required class (adds extra space as necessary)
    if (this.isRequired)
      this.labelClass += this.labelClass.length > 0? " required": "required";
  }

  ngAfterViewInit() {
    // Adds current control to the parent form (in a way that doesn't cause an Angular exception)
    setTimeout(_ => this.addControlToForm());
  }

  addControlToForm() {
    this.parentForm.form.addControl(this.elementName, this.formElement.control);
  }

  update() {
    this.modelChange.emit(this.model);
  }

  // Meant to be called by a parent component containing this element
  public clear() {
    this.formElement.reset();
  }
}