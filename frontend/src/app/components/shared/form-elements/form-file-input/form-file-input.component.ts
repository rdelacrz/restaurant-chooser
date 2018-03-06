import { Component, EventEmitter, Output } from '@angular/core';
import { BaseFormElement } from '../../../../core/components';
import { FileData } from '../../../../view-models';

@Component({
  selector: 'form-file-input',
  templateUrl: './form-file-input.component.html',
  styleUrls: ['./form-file-input.component.scss']
})
export class FormFileInputComponent extends BaseFormElement {
  @Output() fileLoadStarted = new EventEmitter();
  @Output() fileChange = new EventEmitter<FileData>();

  onFileChange(event) {
    this.fileLoadStarted.emit();
    
    // Attempts to read new file, if any
    if (event.target.files && event.target.files.length > 0) {
      let reader = new FileReader();
      let file = event.target.files[0];
      reader.readAsDataURL(file);
      reader.onload = () => {
        let fileData = new FileData(file.name, file.type, reader.result.split(',')[1]);
        this.fileChange.emit(fileData);
      };
    }
    else {
      this.fileChange.emit(null);
    }
  }
}