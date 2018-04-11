import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';

import { ModalComponent } from './modal/modal.component';
import { PageComponent } from './page/page.component';
import { SiteFooterComponent } from './site-footer/site-footer.component';
import { SiteHeaderComponent } from './site-header/site-header.component';

// Form elements
import { FormDropdownComponent } from './form-elements/form-dropdown/form-dropdown.component';
import { FormRowComponent } from './form-elements/form-row/form-row.component';
import { FormTextAreaComponent } from './form-elements/form-textarea/form-textarea.component';
import { FormTextboxComponent } from './form-elements/form-textbox/form-textbox.component';
import { FormFileInputComponent } from './form-elements/form-file-input/form-file-input.component';

@NgModule({
  declarations: [
    ModalComponent,
    PageComponent,
    SiteFooterComponent,
    SiteHeaderComponent,
    FormDropdownComponent,
    FormRowComponent,
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
    PageComponent,
    SiteFooterComponent,
    SiteHeaderComponent,
    FormDropdownComponent,
    FormRowComponent,
    FormTextAreaComponent,
    FormTextboxComponent,
    FormFileInputComponent
  ]
})
export class SharedModule { }
