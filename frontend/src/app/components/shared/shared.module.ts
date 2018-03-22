import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';

import { ModalComponent } from './modal/modal.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import { PageComponent } from './page/page.component';

// Form elements
import { FormTextAreaComponent } from './form-elements/form-textarea/form-textarea.component';
import { FormTextboxComponent } from './form-elements/form-textbox/form-textbox.component';
import { FormFileInputComponent } from './form-elements/form-file-input/form-file-input.component';

@NgModule({
  declarations: [
    ModalComponent,
    NavBarComponent,
    PageComponent,
    FormTextAreaComponent,
    FormTextboxComponent,
    FormFileInputComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    RouterModule
  ],
  exports: [
    ModalComponent,
    NavBarComponent,
    PageComponent,
    FormTextAreaComponent,
    FormTextboxComponent,
    FormFileInputComponent
  ]
})
export class SharedModule { }
