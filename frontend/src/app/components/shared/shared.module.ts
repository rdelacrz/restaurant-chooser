import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';

import { BannerComponent } from './banner/banner.component';
import { ModalComponent } from './modal/modal.component';
import { PageComponent } from './page/page.component';
import { SideNavComponent } from './side-nav/side-nav.component';

// Form elements
import { FormTextAreaComponent } from './form-elements/form-textarea/form-textarea.component';
import { FormTextboxComponent } from './form-elements/form-textbox/form-textbox.component';
import { FormFileInputComponent } from './form-elements/form-file-input/form-file-input.component';

@NgModule({
  declarations: [
    BannerComponent,
    ModalComponent,
    PageComponent,
    SideNavComponent,
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
    BannerComponent,
    ModalComponent,
    PageComponent,
    SideNavComponent,
    FormTextAreaComponent,
    FormTextboxComponent,
    FormFileInputComponent
  ]
})
export class SharedModule { }
