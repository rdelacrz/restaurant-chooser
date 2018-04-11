import { ChangeDetectorRef, EventEmitter, Injectable, Input, OnInit, Output, ViewChild } from '@angular/core';
import { NgForm, NgModel } from '@angular/forms';

@Injectable()
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
  @Input() placeholder: string = "";
  @Input() min: number;
  @Input() max: number;
  @Input() maxLength: number;
  @Input() model: any;

  @Output() modelChange = new EventEmitter<any>();

  // Field classes
  labelClass = "col-form-label";
  fieldClass = "";

  // Other parameters
  registered = false;

  constructor(private changeDetectorRef: ChangeDetectorRef) {}

  ngOnInit() {
    // Adds col-sm classes
    if (this.labelColNum)
      this.labelClass += " col-sm-" + this.labelColNum;
    if (this.fieldColNum)
      this.fieldClass += "col-sm-" + this.fieldColNum;

    // Adds required class (adds extra space as necessary)
    if (this.isRequired)
      this.labelClass += this.labelClass.length > 0? " required": "required";

    // Adds form element control to parent and detects any changes to prevent Angular errors
    this.parentForm.form.addControl(this.elementName, this.formElement.control);
    this.changeDetectorRef.detectChanges();
  }

  update() {
    this.modelChange.emit(this.model);
  }

  // Meant to be called by a parent component containing this element
  public clear() {
    this.formElement.reset();
  }
}